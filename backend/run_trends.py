from app.trend_analysis import analyze_ticket_trends


result = analyze_ticket_trends(
    "../data/sample/support_tickets.csv"
)


print("\n===== TICKET TRENDS =====")

for item in result:
    print(
        item["month"],
        "→",
        item["ticket_count"]
    )