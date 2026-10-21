from app.pattern_detection import detect_patterns


result = detect_patterns(
    "../data/sample/support_tickets.csv"
)

print("\n===== PATTERN DETECTION =====")

print("\nTop Customer Problems:")
for item in result["patterns"]["top_problems"][:10]:
    print(
        item["category"],
        "→",
        item["subcategory"],
        "→",
        item["ticket_count"]
    )

print("\nProblems by Customer Type:")
for item in result["patterns"]["problems_by_customer_type"][:10]:
    print(
        item["category"],
        "→",
        item["customer_type"],
        "→",
        item["ticket_count"]
    )

print("\nProblems by Channel:")
for item in result["patterns"]["problems_by_channel"][:10]:
    print(
        item["category"],
        "→",
        item["channel"],
        "→",
        item["ticket_count"]
    )

print("\nProblems by Team:")
for item in result["patterns"]["problems_by_team"][:10]:
    print(
        item["category"],
        "→",
        item["assigned_team"],
        "→",
        item["ticket_count"]
    )