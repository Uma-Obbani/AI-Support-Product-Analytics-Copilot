import pandas as pd


def calculate_impact(
    baseline_csv_path: str,
    post_csv_path: str
):
    baseline = pd.read_csv(baseline_csv_path)
    post = pd.read_csv(post_csv_path)

    # -----------------------------
    # Payment tickets
    # -----------------------------
    baseline_payment = baseline[
        baseline["category"].str.lower() == "payment"
    ].copy()

    post_payment = post[
        post["category"].str.lower() == "payment"
    ].copy()

    if baseline_payment.empty or post_payment.empty:
        return {
            "status": "ERROR",
            "message": "Payment data is missing from baseline or post dataset."
        }

    # -----------------------------
    # Duplicate Payment Rate
    # -----------------------------
    baseline_duplicate = (
        baseline_payment["ticket_description"]
        .fillna("")
        .str.lower()
        .str.contains("duplicate|charged twice")
        .sum()
    )

    post_duplicate = (
        post_payment["ticket_description"]
        .fillna("")
        .str.lower()
        .str.contains("duplicate|charged twice")
        .sum()
    )

    baseline_duplicate_rate = (
        baseline_duplicate / len(baseline_payment)
    ) * 100

    post_duplicate_rate = (
        post_duplicate / len(post_payment)
    ) * 100

    duplicate_rate_change = (
        post_duplicate_rate - baseline_duplicate_rate
    )

    # -----------------------------
    # SLA Breach Rate
    # -----------------------------
    baseline_sla_rate = (
        baseline_payment["sla_breached"].mean()
    ) * 100

    post_sla_rate = (
        post_payment["sla_breached"].mean()
    ) * 100

    sla_rate_change = (
        post_sla_rate - baseline_sla_rate
    )

    # -----------------------------
    # Average Resolution Time
    # -----------------------------
    baseline_resolution = (
        baseline_payment["resolution_minutes"].mean()
    )

    post_resolution = (
        post_payment["resolution_minutes"].mean()
    )

    resolution_change = (
        post_resolution - baseline_resolution
    )

    if baseline_resolution != 0:
        resolution_percentage_change = (
            resolution_change / baseline_resolution
        ) * 100
    else:
        resolution_percentage_change = None

    # -----------------------------
    # Ticket Volume
    # -----------------------------
    baseline_ticket_volume = len(baseline_payment)
    post_ticket_volume = len(post_payment)

    ticket_volume_change = (
        post_ticket_volume - baseline_ticket_volume
    )

    # -----------------------------
    # Overall assessment
    # -----------------------------
    improvements = 0

    if duplicate_rate_change < 0:
        improvements += 1

    if sla_rate_change < 0:
        improvements += 1

    if resolution_change < 0:
        improvements += 1

    if improvements >= 2:
        assessment = "IMPROVEMENT_SIGNAL"

    elif improvements == 1:
        assessment = "MIXED_RESULT"

    else:
        assessment = "NO_CLEAR_IMPROVEMENT"

    return {
        "status": "SUCCESS",

        "baseline": {
            "payment_ticket_volume": baseline_ticket_volume,
            "duplicate_payment_rate": round(
                baseline_duplicate_rate, 2
            ),
            "sla_breach_rate": round(
                baseline_sla_rate, 2
            ),
            "average_resolution_minutes": round(
                baseline_resolution, 2
            )
        },

        "post_implementation": {
            "payment_ticket_volume": post_ticket_volume,
            "duplicate_payment_rate": round(
                post_duplicate_rate, 2
            ),
            "sla_breach_rate": round(
                post_sla_rate, 2
            ),
            "average_resolution_minutes": round(
                post_resolution, 2
            )
        },

        "change": {
            "ticket_volume_change": ticket_volume_change,
            "duplicate_payment_rate_change_percentage_points":
                round(duplicate_rate_change, 2),
            "sla_breach_rate_change_percentage_points":
                round(sla_rate_change, 2),
            "resolution_time_change_minutes":
                round(resolution_change, 2),
            "resolution_time_change_percentage":
                (
                    round(
                        resolution_percentage_change, 2
                    )
                    if resolution_percentage_change is not None
                    else None
                )
        },

        "assessment": assessment,

        "note": (
            "Impact measurement compares baseline and "
            "post-implementation datasets. It does not by itself "
            "prove causality."
        )
    }