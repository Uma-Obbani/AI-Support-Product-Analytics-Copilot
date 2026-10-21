from app.trend_interpretation import analyze_problem_trend


result = analyze_problem_trend(
    "../data/sample/support_tickets.csv",
    "Payment"
)

print("\n===== PAYMENT TREND =====")

print("Category:", result["category"])

print("\nMonthly ticket volume:")

for item in result["monthly_ticket_volume"]:
    print(
        item["month"],
        "→",
        item["ticket_count"],
        "tickets"
    )

print("\nTrend:", result["trend"])
print("Basis:", result["trend_basis"])