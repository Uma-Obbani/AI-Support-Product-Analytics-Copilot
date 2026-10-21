from app.validation import create_validation_summary


findings = [
    {
        "team": "Support",
        "finding": "Payment tickets require manual investigation.",
        "status": "CONFIRMED"
    },
    {
        "team": "Engineering",
        "finding": "Payment API errors may be contributing to failures.",
        "status": "TO_VALIDATE"
    },
    {
        "team": "Product",
        "finding": "Payment problems may be affecting checkout conversion.",
        "status": "HYPOTHESIS"
    },
    {
        "team": "Business",
        "finding": "Payment issues may have measurable revenue impact.",
        "status": "TO_VALIDATE"
    }
]


result = create_validation_summary(findings)

print("\n===== VALIDATION SUMMARY =====")

print("\nConfirmed Findings:")

for item in result["confirmed_findings"]:
    print(
        item["team"],
        "→",
        item["finding"]
    )

print("\nFindings To Validate:")

for item in result["findings_to_validate"]:
    print(
        item["team"],
        "→",
        item["finding"]
    )

print("\nHypotheses:")

for item in result["hypotheses"]:
    print(
        item["team"],
        "→",
        item["finding"]
    )

print("\nValidation Complete:")
print(result["validation_complete"])