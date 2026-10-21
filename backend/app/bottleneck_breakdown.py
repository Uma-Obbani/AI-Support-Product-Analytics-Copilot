import pandas as pd


def analyze_bottleneck_breakdown(csv_path: str):

    df = pd.read_csv(csv_path)

    breakdown = (
        df.groupby(
            ["category", "subcategory"]
        )
        .agg(
            ticket_count=("ticket_id", "count"),
            avg_first_response_minutes=(
                "first_response_minutes",
                "mean"
            ),
            avg_resolution_minutes=(
                "resolution_minutes",
                "mean"
            ),
            sla_breaches=(
                "sla_breached",
                "sum"
            )
        )
        .reset_index()
    )

    breakdown["sla_breach_rate"] = (
        breakdown["sla_breaches"]
        / breakdown["ticket_count"]
    )

    breakdown = breakdown.sort_values(
        [
            "sla_breach_rate",
            "ticket_count"
        ],
        ascending=[False, False]
    )

    return breakdown.to_dict(
        orient="records"
    )