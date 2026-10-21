from app.bottleneck_breakdown import (
    analyze_bottleneck_breakdown
)


result = analyze_bottleneck_breakdown(
    "../data/sample/support_tickets.csv"
)


print("\n===== BOTTLENECK BREAKDOWN =====")

for item in result:

    print(
        item["category"],
        "→",
        item["subcategory"]
    )

    print(
        "Tickets:",
        item["ticket_count"]
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
        "Avg resolution:",
        round(
            item["avg_resolution_minutes"],
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

    print("-" * 50)