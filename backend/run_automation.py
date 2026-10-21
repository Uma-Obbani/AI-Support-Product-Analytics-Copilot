from app.automation_opportunity import (
    detect_automation_opportunities
)


result = detect_automation_opportunities(
    "../data/sample/support_tickets.csv"
)


print("\n===== AUTOMATION OPPORTUNITIES =====")

for item in result:

    print(
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
        round(
            item["avg_resolution_minutes"],
            2
        ),
        "minutes"
    )

    print(
        "Avg first response:",
        round(
            item["avg_first_response_minutes"],
            2
        ),
        "minutes"
    )

    print(
        "SLA breaches:",
        item["sla_breaches"]
    )

    print(
        "SLA breach rate:",
        round(
            item["sla_breach_rate"] * 100,
            2
        ),
        "%"
    )

    print(
        "Potential automation:",
        item["potential_automation"]
    )

    print("-" * 50)