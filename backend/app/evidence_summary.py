import pandas as pd


def build_evidence_summary(
    support_csv_path: str,
    stakeholder_csv_path: str,
    request_id: str,
    category: str
):
    support = pd.read_csv(support_csv_path)
    stakeholders = pd.read_csv(stakeholder_csv_path)

    # -----------------------------
    # 1. Stakeholder evidence
    # -----------------------------
    request_df = stakeholders[
        stakeholders["request_id"] == request_id
    ]

    if request_df.empty:
        return {
            "request_id": request_id,
            "status": "ERROR",
            "message": "Stakeholder request not found."
        }

    request = request_df.iloc[0]

    # -----------------------------
    # 2. Customer support evidence
    # -----------------------------
    category_df = support[
        support["category"].str.lower() == category.lower()
    ].copy()

    if category_df.empty:
        return {
            "request_id": request_id,
            "status": "ERROR",
            "message": "No support evidence found."
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
    ) * 100

    # -----------------------------
    # 3. Monthly trend
    # -----------------------------
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

    # -----------------------------
    # 4. Evidence status
    # -----------------------------
    if (
        sla_breach_rate >= 30
        or avg_resolution >= 720
    ):
        operational_signal = "STRONG"
    else:
        operational_signal = "NORMAL"

    return {
        "request_id": request_id,

        "stakeholder": {
            "title": request["request_title"],
            "business_goal": request["business_goal"],
            "urgency": request["urgency"],
            "expected_business_impact": request[
                "expected_business_impact"
            ],
            "affected_area": request["affected_area"]
        },

        "customer_support": {
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
                sla_breach_rate, 2
            )
        },

        "trend": {
            "monthly_volume": monthly.to_dict(
                orient="records"
            ),
            "direction": trend,
            "basis": (
                "Latest month compared with "
                "previous available month."
            )
        },

        "assessment": {
            "operational_signal": operational_signal,

            "root_cause": "NOT_ESTABLISHED",

            "business_impact": "NOT_VALIDATED",

            "automation_suitability": "NOT_VALIDATED"
        },

        "po_next_step": (
            "Validate the operational problem with "
            "Support, Product and Engineering before "
            "recommending a solution."
        )
    }