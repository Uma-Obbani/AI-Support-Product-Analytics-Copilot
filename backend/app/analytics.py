
    import pandas as pd


def analyze_ticket_patterns(csv_path: str):

    df = pd.read_csv(csv_path)

    category_counts = (
        df["category"]
        .value_counts()
        .reset_index()
    )

    category_counts.columns = [
        "category",
        "ticket_count"
    ]

    subcategory_counts = (
        df.groupby(
            ["category", "subcategory"]
        )
        .size()
        .reset_index(name="ticket_count")
        .sort_values(
            "ticket_count",
            ascending=False
        )
    )

    return {
        "total_tickets": len(df),
        "category_counts": category_counts.to_dict(
            orient="records"
        ),
        "subcategory_counts": subcategory_counts.to_dict(
            orient="records"
        )
    }


def analyze_ticket_trends(csv_path: str):

    df = pd.read_csv(csv_path)

    df["created_at"] = pd.to_datetime(
        df["created_at"]
    )

    monthly_trends = (
        df.groupby(
            df["created_at"].dt.to_period("M")
        )
        .size()
        .reset_index(name="ticket_count")
    )

    monthly_trends["month"] = (
        monthly_trends["created_at"]
        .astype(str)
    )

    monthly_trends = monthly_trends[
        ["month", "ticket_count"]
    ]

    return monthly_trends.to_dict(
        orient="records"
    )