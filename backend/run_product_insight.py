from app.product_insights import generate_product_insight


result = generate_product_insight(
    "../data/sample/support_tickets.csv",
    "../data/sample/stakeholder_requests.csv",
    "REQ-0004",
    "Payment"
)

print("\n===== PRODUCT INSIGHT =====")

print("\nStakeholder Request:")
for key, value in result["stakeholder_request"].items():
    print(key, "→", value)

print("\nCustomer Evidence:")
for key, value in result["customer_evidence"].items():
    print(key, "→", value)

print("\nSignal:")
for key, value in result["signal"].items():
    print(key, "→", value)

print("\nKnown:")
for item in result["known"]:
    print("→", item)

print("\nUnknown:")
for item in result["unknown"]:
    print("→", item)

print("\nHypothesis:")
print("→", result["hypothesis"])

print("\nPotential Product Opportunity:")
print("→", result["potential_product_opportunity"])