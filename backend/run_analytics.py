from app.analytics import analyze_ticket_patterns

result = analyze_ticket_patterns(
    "../data/sample/support_tickets.csv"
)

print("\n===== TICKET ANALYTICS =====")

print("\nTotal tickets:")
print(result["total_tickets"])

print("\nTickets by category:")
for item in result["category_counts"]:
    print(item["category"], "→", item["ticket_count"])

print("\nTickets by subcategory:")
for item in result["subcategory_counts"]:
    print(
        item["category"],
        "→",
        item["subcategory"],
        "→",
        item["ticket_count"]
    )