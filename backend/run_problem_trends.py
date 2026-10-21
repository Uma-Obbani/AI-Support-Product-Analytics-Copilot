from app.problem_trends import analyze_problem_trends


result = analyze_problem_trends(
    "../data/sample/support_tickets.csv"
)


print("\n===== PROBLEM TRENDS =====")

for item in result:
    print(
        item["month"],
        "→",
        item["category"],
        "→",
        item["subcategory"],
        "→",
        item["ticket_count"]
    )