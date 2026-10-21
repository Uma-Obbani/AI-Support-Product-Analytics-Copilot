import pandas as pd


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