import pandas as pd


def analyze_problem_trends(csv_path: str):

    df = pd.read_csv(csv_path)

    df["created_at"] = pd.to_datetime(
        df["created_at"]
    )

    df["month"] = (
        df["created_at"]
        .dt.to_period("M")
        .astype(str)
    )

    problem_trends = (
        df.groupby(
            ["month", "category", "subcategory"]
        )
        .size()
        .reset_index(name="ticket_count")
        .sort_values(
            ["month", "ticket_count"],
            ascending=[True, False]
        )
    )

    return problem_trends.to_dict(
        orient="records"
    )