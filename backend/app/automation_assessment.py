import pandas as pd


def assess_automation_opportunities(csv_path: str):

    df = pd.read_csv(csv_path)

    assessment = (
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

    assessment["sla_breach_rate"] = (
        assessment["sla_breaches"]
        / assessment["ticket_count"]
    )

    results = []

    for _, row in assessment.iterrows():

        operational_pain = (
            row["sla_breach_rate"] >= 0.30
            or row["avg_resolution_minutes"] >= 720
        )

        if operational_pain:
            pain_level = "HIGH"
        else:
            pain_level = "LOW"

        results.append({
            "category": row["category"],
            "subcategory": row["subcategory"],
            "assigned_team": row["assigned_team"],
            "ticket_count": int(row["ticket_count"]),
            "avg_resolution_minutes": round(
                row["avg_resolution_minutes"], 2
            ),
            "sla_breach_rate": round(
                row["sla_breach_rate"] * 100, 2
            ),
            "operational_pain": pain_level,
            "automation_suitability": "UNKNOWN",
            "reason": (
                "Operational pain is present, but the current "
                "dataset does not contain enough evidence about "
                "repetitive work, manual effort, or decision complexity."
                if operational_pain
                else
                "Current data does not show a strong operational pain signal."
            ),
            "recommendation": (
                "Collect process-level evidence before recommending automation."
                if operational_pain
                else
                "No immediate automation investigation required."
            )
        })

    return results