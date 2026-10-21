import json
import pandas as pd

from app.classifier import classify_ticket


def evaluate_classifier(csv_path: str):

    df = pd.read_csv(csv_path)

    results = []

    for _, row in df.iterrows():

        prediction = classify_ticket(row["ticket_description"])

        results.append({
            "ticket_id": row["ticket_id"],
            "expected_category": row["category"],
            "predicted_category": prediction["predicted_category"],
            "expected_subcategory": row["subcategory"],
            "predicted_subcategory": prediction["predicted_subcategory"],
            "confidence": prediction["confidence"]
        })

    results_df = pd.DataFrame(results)

    category_accuracy = (
        results_df["expected_category"]
        == results_df["predicted_category"]
    ).mean()

    subcategory_accuracy = (
        results_df["expected_subcategory"]
        == results_df["predicted_subcategory"]
    ).mean()

    invalid_predictions = results_df[
        ~results_df["predicted_category"].isin(df["category"].unique())
    ]

    return {
        "total_tickets": len(results_df),
        "category_accuracy": round(category_accuracy, 4),
        "subcategory_accuracy": round(subcategory_accuracy, 4),
        "invalid_predictions": len(invalid_predictions),
        "average_confidence": round(
            results_df["confidence"].mean(), 4
        ),
        "results": results_df
    }