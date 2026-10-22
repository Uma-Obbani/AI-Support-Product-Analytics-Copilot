from app.product_prioritization import prioritize_product_problems


result = prioritize_product_problems(
    "../data/sample/support_tickets.csv",
    "../data/sample/stakeholder_requests.csv"
)


print("\n===== PRODUCT PRIORITIZATION =====")

for index, problem in enumerate(
    result["product_prioritization"],
    start=1
):

    print(f"\n{index}. {problem['problem']}")

    print(
        "Priority →",
        problem["priority"]
    )

    print(
        "Decision →",
        problem["decision"]
    )

    print(
        "Score →",
        problem["score"]
    )

    print(
        "Tickets →",
        problem["ticket_count"]
    )

    print(
        "Average Resolution →",
        problem["avg_resolution_minutes"],
        "minutes"
    )

    print(
        "SLA Breach Rate →",
        problem["sla_breach_rate"],
        "%"
    )

    print(
        "Trend →",
        problem["trend"]
    )

    print(
        "Stakeholder Requests →",
        problem["stakeholder_requests"]
    )

    print("Reasons:")

    for reason in problem["reasons"]:
        print("  →", reason)


print("\n===== PRINCIPLE =====")
print(result["principle"])

print("\n===== LIMITATIONS =====")

for limitation in result["limitations"]:
    print("→", limitation)