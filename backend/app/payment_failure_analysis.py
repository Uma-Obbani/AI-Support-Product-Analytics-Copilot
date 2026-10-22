import pandas as pd


def analyze_payment_failure_patterns(csv_path: str):
    df = pd.read_csv(csv_path)

    # Only Payment tickets
    payment_df = df[
        df["category"].str.lower() == "payment"
    ].copy()

    if payment_df.empty:
        return {
            "status": "ERROR",
            "message": "No payment tickets found."
        }

    # Normalize ticket descriptions
    payment_df["description"] = (
        payment_df["ticket_description"]
        .fillna("")
        .str.lower()
        .str.strip()
    )

    def classify_problem(description):
        if "pending" in description:
            return "Payment Pending"

        if "duplicate" in description or "charged twice" in description:
            return "Duplicate Payment"

        if (
            "failed" in description
            or "declined" in description
            or "rejected" in description
        ):
            return "Payment Failed"

        if "refund" in description:
            return "Payment Refund Issue"

        return "UNKNOWN"

    payment_df["observed_problem"] = (
        payment_df["description"]
        .apply(classify_problem)
    )

    # Count observed customer-reported patterns
    patterns = (
        payment_df["observed_problem"]
        .value_counts()
        .reset_index()
    )

    patterns.columns = [
        "observed_problem",
        "ticket_count"
    ]

    total_tickets = len(payment_df)

    patterns["percentage"] = (
        patterns["ticket_count"] / total_tickets * 100
    ).round(2)

    # Root causes are NOT established by ticket descriptions alone
    patterns["status"] = patterns[
        "observed_problem"
    ].apply(
        lambda x:
            "UNKNOWN"
            if x == "UNKNOWN"
            else "OBSERVED_CUSTOMER_PATTERN"
    )

    return {
        "status": "SUCCESS",

        "total_payment_tickets": total_tickets,

        "observed_patterns": (
            patterns.to_dict(orient="records")
        ),

        "root_cause_status": "TO_VALIDATE",

        "root_cause_note": (
            "Ticket descriptions identify customer-reported "
            "problem patterns but do not establish technical "
            "or process root causes."
        )
    }