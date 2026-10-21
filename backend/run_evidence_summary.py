from app.evidence_summary import build_evidence_summary


result = build_evidence_summary(
    "../data/sample/support_tickets.csv",
    "../data/sample/stakeholder_requests.csv",
    "REQ-0004",
    "Payment"
)

print("\n===== PO EVIDENCE SUMMARY =====")

print("\nRequest ID:")
print(result["request_id"])

print("\nStakeholder:")
for key, value in result["stakeholder"].items():
    print(key, "→", value)

print("\nCustomer Support:")
for key, value in result["customer_support"].items():
    print(key, "→", value)

print("\nTrend:")
print("Direction →", result["trend"]["direction"])

for item in result["trend"]["monthly_volume"]:
    print(
        item["month"],
        "→",
        item["ticket_count"],
        "tickets"
    )

print("\nAssessment:")
for key, value in result["assessment"].items():
    print(key, "→", value)

print("\nPO Next Step:")
print("→", result["po_next_step"])