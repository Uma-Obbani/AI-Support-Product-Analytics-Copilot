from app.payment_failure_analysis import (
    analyze_payment_failure_patterns
)


result = analyze_payment_failure_patterns(
    "../data/sample/support_tickets.csv"
)


print("\n===== PAYMENT FAILURE ANALYSIS =====")

print(
    "\nTotal Payment Tickets →",
    result["total_payment_tickets"]
)

print("\nObserved Customer Problem Patterns:")

for pattern in result["observed_patterns"]:

    print(
        pattern["observed_problem"],
        "→",
        pattern["ticket_count"],
        "tickets",
        "(",
        pattern["percentage"],
        "% )",
        "→",
        pattern["status"]
    )

print(
    "\nRoot Cause Status →",
    result["root_cause_status"]
)

print(
    "Root Cause Note →",
    result["root_cause_note"]
)