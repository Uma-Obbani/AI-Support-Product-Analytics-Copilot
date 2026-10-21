from app.stakeholder_insights import (
    analyze_stakeholder_request
)


result = analyze_stakeholder_request(
    "../data/sample/stakeholder_requests.csv",
    "../data/sample/support_tickets.csv",
    "REQ-0004"
)


print("\n===== STAKEHOLDER INSIGHT =====")

print("\nRequest:")

for key, value in result["request"].items():
    print(
        key,
        "→",
        value
    )

print(
    "\nMatched categories:",
    result["matched_categories"]
)

print("\nSupport evidence:")

for item in result["support_evidence"]:

    print(
        item["support_category"],
        "→",
        item["ticket_count"],
        "tickets"
    )

    print(
        "Average resolution:",
        item["avg_resolution_minutes"],
        "minutes"
    )

    print(
        "SLA breaches:",
        item["sla_breaches"]
    )

    print(
        "SLA breach rate:",
        item["sla_breach_rate"],
        "%"
    )