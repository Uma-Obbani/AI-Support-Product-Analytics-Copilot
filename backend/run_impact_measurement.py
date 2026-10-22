from app.impact_measurement import calculate_impact


result = calculate_impact(
    "../data/sample/support_tickets.csv",
    "../data/sample/post_implementation_support_tickets.csv"
)


print("\n===== IMPACT MEASUREMENT =====")

print("\nBaseline:")
for key, value in result["baseline"].items():
    print(key, "→", value)

print("\nPost Implementation:")
for key, value in result["post_implementation"].items():
    print(key, "→", value)

print("\nChange:")
for key, value in result["change"].items():
    print(key, "→", value)

print("\nAssessment:")
print("→", result["assessment"])

print("\nNote:")
print("→", result["note"])