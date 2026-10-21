from app.root_cause_analysis import (
    analyze_bottleneck_root_causes
)


result = analyze_bottleneck_root_causes(
    "../data/sample/support_tickets.csv",
    "Subscription",
    "Subscription Cancellation"
)


print("\n===== ROOT CAUSE INVESTIGATION =====")

print(
    "\nProblem:",
    result["category"],
    "→",
    result["subcategory"]
)

print(
    "\nTotal tickets:",
    result["total_tickets"]
)


for dimension in [
    "by_customer_type",
    "by_channel",
    "by_status",
    "by_team"
]:

    print(
        "\n---",
        dimension,
        "---"
    )

    for item in result[dimension]:

        print(item)