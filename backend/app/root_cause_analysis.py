import pandas as pd


def analyze_bottleneck_root_causes(
    csv_path: str,
    category: str,
    subcategory: str
):
    df = pd.read_csv(csv_path)

    # Focus only on the selected bottleneck
    bottleneck_df = df[
        (df["category"] == category)
        & (df["subcategory"] == subcategory)
    ].copy()

    if bottleneck_df.empty:
        return {
            "category": category,
            "subcategory": subcategory,
            "message": "No matching tickets found."
        }

    def analyze_dimension(column):
        result = (
            bottleneck_df.groupby(column)
            .agg(
                ticket_count=("ticket_id", "count"),
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

        result["sla_breach_rate"] = (
            result["sla_breaches"]
            / result["ticket_count"]
        )

        return result.to_dict(orient="records")

    return {
        "category": category,
        "subcategory": subcategory,
        "total_tickets": len(bottleneck_df),

        "by_customer_type": analyze_dimension(
            "customer_type"
        ),

        "by_channel": analyze_dimension(
            "channel"
        ),

        "by_status": analyze_dimension(
            "current_status"
        ),

        "by_team": analyze_dimension(
            "assigned_team"
        )
    }