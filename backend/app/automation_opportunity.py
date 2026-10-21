import pandas as pd


def detect_automation_opportunities(csv_path: str):

    df = pd.read_csv(csv_path)

    opportunities = (
        df.groupby(
            ["category", "subcategory", "assigned_team"]
        )
        .agg(
            ticket_count=("ticket_id", "count"),
            avg_resolution_minutes=(
                "resolution_minutes",
                "mean"
            ),
            avg_first_response_minutes=(
                "first_response_minutes",
                "mean"
            ),
            sla_breaches=(
                "sla_breached",
                "sum"
            )
        )
        .reset_index()
    )

    opportunities["sla_breach_rate"] = (
        opportunities["sla_breaches"]
        / opportunities["ticket_count"]
    )

    # Initial development criteria
    opportunities["potential_automation"] = (
        (opportunities["ticket_count"] >= 15)
        &
        (
            opportunities["avg_resolution_minutes"]
            >= 720
        )
        &
        (
            opportunities["sla_breach_rate"]
            >= 0.30
        )
    )

    opportunities = opportunities.sort_values(
        [
            "potential_automation",
            "ticket_count",
            "sla_breach_rate"
        ],
        ascending=[False, False, False]
    )

    return opportunities.to_dict(
        orient="records"
    )