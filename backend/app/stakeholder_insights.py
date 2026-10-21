import pandas as pd


def analyze_stakeholder_request(
    stakeholder_csv_path: str,
    support_csv_path: str,
    request_id: str
):
    stakeholders = pd.read_csv(
        stakeholder_csv_path
    )

    support = pd.read_csv(
        support_csv_path
    )

    request = stakeholders[
        stakeholders["request_id"] == request_id
    ]

    if request.empty:
        return {
            "request_id": request_id,
            "message": "Stakeholder request not found."
        }

    request = request.iloc[0]

    request_text = (
        str(request["request_title"])
        + " "
        + str(request["request_description"])
        + " "
        + str(request["business_goal"])
    ).lower()

    # Simple keyword-based evidence matching.
    # This is intentionally deterministic for the first version.
    keyword_mapping = {
        "payment": ["payment", "pay", "checkout"],
        "delivery": ["delivery", "shipping", "package"],
        "subscription": ["subscription", "renewal", "cancel"],
        "account": ["account", "login", "password"],
        "refund": ["refund", "money back"],
        "order": ["order", "purchase"],
        "product": ["product", "item"],
        "technical": ["technical", "app", "website", "error"]
    }

    matched_categories = []

    for category, keywords in keyword_mapping.items():

        if any(
            keyword in request_text
            for keyword in keywords
        ):
            matched_categories.append(category)

    evidence = []

    for category in matched_categories:

        category_support = support[
            support["category"]
            .str.lower()
            .str.contains(category, na=False)
        ]

        if category_support.empty:
            continue

        evidence.append({
            "support_category": category,
            "ticket_count": len(category_support),
            "avg_resolution_minutes": round(
                category_support[
                    "resolution_minutes"
                ].mean(),
                2
            ),
            "sla_breaches": int(
                category_support[
                    "sla_breached"
                ].sum()
            ),
            "sla_breach_rate": round(
                category_support[
                    "sla_breached"
                ].mean() * 100,
                2
            )
        })

    return {
        "request": {
            "request_id": request["request_id"],
            "title": request["request_title"],
            "business_goal": request["business_goal"],
            "urgency": request["urgency"],
            "expected_business_impact": (
                request["expected_business_impact"]
            ),
            "affected_area": request["affected_area"]
        },

        "matched_categories": matched_categories,

        "support_evidence": evidence
    }