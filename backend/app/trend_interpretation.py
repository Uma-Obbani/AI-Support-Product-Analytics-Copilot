import pandas as pd


def analyze_problem_trend(
    csv_path: str,
    category: str,
    subcategory: str = None
):
    df = pd.read_csv(csv_path)

    df["created_at"] = pd.to_datetime(df["created_at"])
    df["month"] = df["created_at"].dt.to_period("M").astype(str)

    # Filter category
    filtered = df[
        df["category"].str.lower() == category.lower()
    ].copy()

    # Optional subcategory filter
    if subcategory:
        filtered = filtered[
            filtered["subcategory"].str.lower()
            == subcategory.lower()
        ]

    if filtered.empty:
        return {
            "category": category,
            "subcategory": subcategory,
            "message": "No matching data found."
        }

    monthly = (
        filtered
        .groupby("month")
        .size()
        .reset_index(name="ticket_count")
        .sort_values("month")
    )

    counts = monthly["ticket_count"].tolist()

    # Need at least two months to determine direction
    if len(counts) < 2:
        trend = "INSUFFICIENT_DATA"
    elif counts[-1] > counts[-2]:
        trend = "INCREASING"
    elif counts[-1] < counts[-2]:
        trend = "DECREASING"
    else:
        trend = "STABLE"

    return {
        "category": category,
        "subcategory": subcategory,
        "monthly_ticket_volume": monthly.to_dict(
            orient="records"
        ),
        "trend": trend,
        "trend_basis": (
            "Trend is based on comparison of the latest "
            "two available months."
        )
    }