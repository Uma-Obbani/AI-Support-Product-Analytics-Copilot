import pandas as pd


def detect_bottlenecks(csv_path: str):

    df = pd.read_csv(csv_path)

    # Aggregate support performance by category and assigned team
    bottlenecks = (
        df.groupby(
            ["category", "assigned_team"]
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

    # Calculate SLA breach rate
    bottlenecks["sla_breach_rate"] = (
        bottlenecks["sla_breaches"]
        / bottlenecks["ticket_count"]
    )

    # Identify potential bottlenecks
    bottlenecks["potential_bottleneck"] = (
        (bottlenecks["sla_breach_rate"] >= 0.30)
        |
        (bottlenecks["avg_resolution_minutes"] >= 720)
    )

    # Sort most problematic areas first
    bottlenecks = bottlenecks.sort_values(
        [
            "potential_bottleneck",
            "sla_breach_rate",
            "avg_resolution_minutes"
        ],
        ascending=[False, False, False]
    )

    return bottlenecks.to_dict(
        orient="records"
    )