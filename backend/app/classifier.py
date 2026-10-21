import os
import json
from typing import Dict

from dotenv import load_dotenv
from google import genai

load_dotenv()

CATEGORIES = {
    "Payment": [
        "Payment Failed",
        "Payment Pending",
        "Duplicate Charge",
    ],
    "Delivery": [
        "Late Delivery",
        "Missing Package",
        "Wrong Delivery Address",
    ],
    "Account": [
        "Login Problem",
        "Password Reset",
        "Account Locked",
    ],
    "Technical Issue": [
        "App Error",
        "Website Error",
        "Integration Error",
    ],
    "Product Issue": [
        "Product Defect",
        "Wrong Product Information",
        "Product Not Working",
    ],
    "Refund": [
        "Refund Delayed",
        "Refund Request",
        "Incorrect Refund",
    ],
    "Order": [
        "Order Cancellation",
        "Order Modification",
        "Order Status",
    ],
    "Subscription": [
        "Subscription Cancellation",
        "Renewal Problem",
        "Plan Change",
    ],
}

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def classify_ticket(ticket_description: str) -> Dict:

    allowed_categories = list(CATEGORIES.keys())

    prompt = f"""
You are a customer support ticket classification system.

Classify the following ticket:

TICKET:
{ticket_description}

You MUST choose exactly ONE category from this list:

{allowed_categories}

The available subcategories are:

{json.dumps(CATEGORIES, indent=2)}

Return ONLY valid JSON in exactly this format:

{{
    "predicted_category": "Payment",
    "predicted_subcategory": "Payment Failed",
    "confidence": 0.95,
    "reasoning": "The ticket describes a failed payment."
}}

STRICT RULES:

1. predicted_category MUST be one of:
{allowed_categories}

2. predicted_subcategory MUST belong to the selected category.

3. confidence MUST be a number between 0 and 1.

4. Do NOT invent categories.

5. Do NOT invent subcategories.

6. Do NOT return Python code.

7. Do NOT return markdown.

8. Do NOT return ```json.

9. Return ONLY the JSON object.

10. The reasoning must be a short explanation, not a detailed chain of thought.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    raw_response = response.text.strip()

    # Remove markdown fences if Gemini unexpectedly adds them
    if raw_response.startswith("```json"):
        raw_response = raw_response[7:]

    if raw_response.startswith("```"):
        raw_response = raw_response[3:]

    if raw_response.endswith("```"):
        raw_response = raw_response[:-3]

    raw_response = raw_response.strip()

    # Convert JSON text into Python dictionary
    result = json.loads(raw_response)

    # -----------------------------
    # VALIDATION
    # -----------------------------

    category = result.get("predicted_category")
    subcategory = result.get("predicted_subcategory")
    confidence = result.get("confidence")

    # Validate category
    if category not in CATEGORIES:
        raise ValueError(
            f"Invalid category returned by AI: {category}"
        )

    # Validate subcategory
    if subcategory not in CATEGORIES[category]:
        raise ValueError(
            f"Invalid subcategory '{subcategory}' for category '{category}'"
        )

    # Validate confidence
    if not isinstance(confidence, (int, float)):
        raise ValueError("Confidence must be a number.")

    if not 0 <= confidence <= 1:
        raise ValueError("Confidence must be between 0 and 1.")

    return result