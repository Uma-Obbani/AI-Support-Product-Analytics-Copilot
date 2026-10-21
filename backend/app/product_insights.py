import pandas as pd


def generate_product_insight(
    support_csv_path: str,
    stakeholder_csv_path: str,
    request_id: str,
    category: str
):
    support = pd.read_csv(support_csv_path)
    stakeholders = pd.read_csv(stakeholder_csv_path)

    # -----------------------------
    # 1. Find stakeholder request
    # -----------------------------
    request_df = stakeholders[
        stakeholders["request_id"] == request_id
    ]

    if request_df.empty:
        return {
            "request_id": request_id,
            "message": "Stakeholder request not found."
        }

    request = request_df.iloc[0]

    # -----------------------------
    # 2. Find customer evidence
    # -----------------------------
    category_df = support[
        support["category"].str.lower() == category.lower()
    ].copy()

    if category_df.empty:
        return {
            "request_id": request_id,
            "category": category,
            "message": "No matching customer support evidence found."
        }

    ticket_count = len(category_df)

    avg_resolution = category_df[
        "resolution_minutes"
    ].mean()

    avg_first_response = category_df[
        "first_response_minutes"
    ].mean()

    sla_breaches = category_df[
        "sla_breached"
    ].sum()

    sla_breach_rate = (
        sla_breaches / ticket_count
    )

    # -----------------------------
    # 3. Determine operational signal
    # -----------------------------
    if (
        sla_breach_rate >= 0.30
        or avg_resolution >= 720
    ):
        operational_signal = "Strong operational pain"
    else:
        operational_signal = "No strong operational pain signal"

    # -----------------------------
    # 4. Analyze monthly trend
    # -----------------------------
    category_df["month"] = (
        pd.to_datetime(category_df["created_at"])
        .dt.to_period("M")
        .astype(str)
    )

    monthly_trend = (
        category_df
        .groupby("month")
        .size()
        .reset_index(name="ticket_count")
        .sort_values("month")
    )

    counts = monthly_trend["ticket_count"].tolist()

    if len(counts) < 2:
        trend = "INSUFFICIENT_DATA"
    elif counts[-1] > counts[-2]:
        trend = "INCREASING"
    elif counts[-1] < counts[-2]:
        trend = "DECREASING"
    else:
        trend = "STABLE"

    # -----------------------------
    # 5. Build product insight
    # -----------------------------
    return {
        "stakeholder_request": {
            "request_id": request["request_id"],
            "title": request["request_title"],
            "business_goal": request["business_goal"],
            "urgency": request["urgency"],
            "expected_business_impact": request[
                "expected_business_impact"
            ],
            "affected_area": request["affected_area"]
        },

        "customer_evidence": {
            "category": category,
            "ticket_count": ticket_count,
            "avg_first_response_minutes": round(
                avg_first_response, 2
            ),
            "avg_resolution_minutes": round(
                avg_resolution, 2
            ),
            "sla_breaches": int(sla_breaches),
            "sla_breach_rate": round(
                sla_breach_rate * 100, 2
            )
        },

        "trend": {
            "monthly_ticket_volume": monthly_trend.to_dict(
                orient="records"
            ),
            "direction": trend,
            "basis": (
                "Latest month compared with the "
                "previous available month."
            )
        },

        "signal": {
            "operational_signal": operational_signal
        },

        "known": [
            f"{ticket_count} customer support tickets "
            f"are related to {category}.",

            f"The average resolution time is "
            f"{round(avg_resolution, 2)} minutes.",

            f"The SLA breach rate is "
            f"{round(sla_breach_rate * 100, 2)}%.",

            f"The latest monthly ticket trend is "
            f"{trend.lower()}."
        ],

        "unknown": [
            "Root cause is not established.",
            "Customer impact is not directly measured.",
            "Business impact is not directly measured.",
            "It is not yet known whether the problem is primarily "
            "product-related or process-related.",
            "Automation suitability requires additional "
            "process-level evidence."
        ],

        "hypothesis": (
            f"{category}-related customer or support-process friction "
            "may be contributing to operational inefficiency. "
            f"The latest available ticket trend is {trend.lower()}, "
            "which strengthens the case for further investigation."
        ),

        "potential_product_opportunity": (
            f"Investigate the {category.lower()} customer journey "
            "and support process to identify opportunities "
            "for simplification, product improvement, or automation."
        )
    }