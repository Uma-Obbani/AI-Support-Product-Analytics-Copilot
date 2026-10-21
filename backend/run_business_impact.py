from app.business_impact import assess_business_impact


result = assess_business_impact(

    customer_impact={
        "status": "TO_VALIDATE",
        "description": "Payment problems may affect customers' ability to complete purchases."
    },

    revenue_impact={
        "status": "TO_VALIDATE",
        "description": "Potential revenue impact from failed payment transactions."
    },

    conversion_impact={
        "status": "TO_VALIDATE",
        "description": "Payment problems may affect checkout conversion."
    },

    operational_cost={
        "status": "VALIDATED",
        "description": "Payment support tickets require significant support handling effort."
    },

    strategic_importance={
        "status": "TO_VALIDATE",
        "description": "Payment experience may be strategically important to the business."
    }
)


print("\n===== BUSINESS IMPACT ASSESSMENT =====")

print("\nOverall Status:")
print("→", result["overall_status"])

print("\nValidated Impacts:")
for item in result["validated_impacts"]:
    print(
        item["area"],
        "→",
        item["value"]["description"]
    )

print("\nImpacts To Validate:")
for item in result["impacts_to_validate"]:
    print(
        item["area"],
        "→",
        item["value"]["description"]
    )

print("\nUnavailable:")
for item in result["unavailable_impacts"]:
    print("→", item)