import pandas as pd


def prioritize_product_problems(
    support_csv_path: str,
    stakeholder_csv_path: str
):
    support = pd.read_csv(support_csv_path)
    stakeholders = pd.read_csv(stakeholder_csv_path)

    results = []

    # --------------------------------
    # 1. Analyze each product problem
    # --------------------------------
    for category in support["category"].dropna().unique():

        category_df = support[
            support["category"] == category
        ].copy()

        ticket_count = len(category_df)

        avg_resolution = category_df[
            "resolution_minutes"
        ].mean()

        sla_breach_rate = (
            category_df["sla_breached"].mean() * 100
        )

        # --------------------------------
        # 2. Determine recent trend
        # --------------------------------
        category_df["month"] = (
            pd.to_datetime(category_df["created_at"])
            .dt.to_period("M")
            .astype(str)
        )

        monthly = (
            category_df
            .groupby("month")
            .size()
            .reset_index(name="ticket_count")
            .sort_values("month")
        )

        counts = monthly["ticket_count"].tolist()

        if len(counts) < 2:
            trend = "INSUFFICIENT_DATA"
        elif counts[-1] > counts[-2]:
            trend = "INCREASING"
        elif counts[-1] < counts[-2]:
            trend = "DECREASING"
        else:
            trend = "STABLE"

        # --------------------------------
        # 3. Check stakeholder demand
        # --------------------------------
        category_text = category.lower()

        matching_requests = stakeholders[
            (
                stakeholders["request_title"]
                .fillna("")
                .str.lower()
                .str.contains(category_text)
            )
            |
            (
                stakeholders["request_description"]
                .fillna("")
                .str.lower()
                .str.contains(category_text)
            )
            |
            (
                stakeholders["business_goal"]
                .fillna("")
                .str.lower()
                .str.contains(category_text)
            )
        ]

        stakeholder_requests = len(matching_requests)

        # --------------------------------
        # 4. Build transparent score
        # --------------------------------
        score = 0
        reasons = []

        # Ticket volume
        if ticket_count >= 50:
            score += 2
            reasons.append("High ticket volume")
        elif ticket_count >= 30:
            score += 1

        # SLA
        if sla_breach_rate >= 50:
            score += 3
            reasons.append("High SLA breach rate")
        elif sla_breach_rate >= 30:
            score += 2
            reasons.append("Elevated SLA breach rate")

        # Resolution time
        if avg_resolution >= 1440:
            score += 3
            reasons.append("Very high resolution time")
        elif avg_resolution >= 720:
            score += 2
            reasons.append("High resolution time")

        # Trend
        if trend == "INCREASING":
            score += 2
            reasons.append("Increasing recent trend")

        # Stakeholder demand
        if stakeholder_requests > 0:
            score += 2
            reasons.append("Stakeholder demand exists")

        # --------------------------------
        # 5. Priority mapping
        # --------------------------------
        if score >= 9:
            priority = "HIGH"
        elif score >= 5:
            priority = "MEDIUM"
        else:
            priority = "LOW"

        # --------------------------------
        # 6. PO recommendation
        # --------------------------------
        if priority == "HIGH":
            decision = "INVESTIGATE"
        elif priority == "MEDIUM":
            decision = "CONSIDER"
        else:
            decision = "MONITOR"

        results.append({
            "problem": category,
            "ticket_count": ticket_count,
            "avg_resolution_minutes": round(
                avg_resolution, 2
            ),
            "sla_breach_rate": round(
                sla_breach_rate, 2
            ),
            "trend": trend,
            "stakeholder_requests": stakeholder_requests,
            "score": score,
            "priority": priority,
            "decision": decision,
            "reasons": reasons
        })

    # --------------------------------
    # 7. Rank problems
    # --------------------------------
    results = sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )

    return {
        "status": "SUCCESS",
        "product_prioritization": results,
        "principle": (
            "Priority is a recommendation based on available "
            "evidence. The Product Owner makes the final decision."
        ),
        "limitations": [
            "Business impact is not directly measured.",
            "Root cause is not automatically established.",
            "Stakeholder demand does not prove customer impact.",
            "The scoring thresholds are development rules, "
            "not universal business standards."
        ]
    }