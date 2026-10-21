from app.evaluation import evaluate_classifier


result = evaluate_classifier(
    "../data/sample/support_tickets.csv"
)

print("\n===== CLASSIFIER EVALUATION =====")
print("Total tickets:", result["total_tickets"])
print("Category accuracy:", result["category_accuracy"])
print("Subcategory accuracy:", result["subcategory_accuracy"])
print("Invalid predictions:", result["invalid_predictions"])
print("Average confidence:", result["average_confidence"])