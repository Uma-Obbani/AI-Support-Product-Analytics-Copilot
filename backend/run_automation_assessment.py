from app.automation_assessment import (
    assess_automation_opportunities
)


result = assess_automation_opportunities(
    "../data/sample/support_tickets.csv"
)


print("\n===== AUTOMATION ASSESSMENT =====")

for item in result:

    print(
        "\n",
        item["category"],
        "→",
        item["subcategory"],
        "→",
        item["assigned_team"]
    )

    print(
        "Tickets:",
        item["ticket_count"]
    )

    print(
        "Avg resolution:",
        item["avg_resolution_minutes"],
        "minutes"
    )

    print(
        "SLA breach rate:",
        item["sla_breach_rate"],
        "%"
    )

    print(
        "Operational pain:",
        item["operational_pain"]
    )

    print(
        "Automation suitability:",
        item["automation_suitability"]
    )

    print(
        "Reason:",
        item["reason"]
    )

    print(
        "Recommendation:",
        item["recommendation"]
    )

    print("-" * 60)