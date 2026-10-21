import pandas as pd


def detect_patterns(csv_path: str):

    df = pd.read_csv(csv_path)

    patterns = {}

    # 1. Most frequent category/subcategory combinations
    patterns["top_problems"] = (
        df.groupby(["category", "subcategory"])
        .size()
        .reset_index(name="ticket_count")
        .sort_values("ticket_count", ascending=False)
        .to_dict(orient="records")
    )

    # 2. Problems by customer type
    patterns["problems_by_customer_type"] = (
        df.groupby(["category", "customer_type"])
        .size()
        .reset_index(name="ticket_count")
        .sort_values("ticket_count", ascending=False)
        .to_dict(orient="records")
    )

    # 3. Problems by channel
    patterns["problems_by_channel"] = (
        df.groupby(["category", "channel"])
        .size()
        .reset_index(name="ticket_count")
        .sort_values("ticket_count", ascending=False)
        .to_dict(orient="records")
    )

    # 4. Problems by assigned team
    patterns["problems_by_team"] = (
        df.groupby(["category", "assigned_team"])
        .size()
        .reset_index(name="ticket_count")
        .sort_values("ticket_count", ascending=False)
        .to_dict(orient="records")
    )

    # 5. Customer impact distribution
    patterns["customer_impact"] = (
        df.groupby(["category", "customer_impact"])
        .size()
        .reset_index(name="ticket_count")
        .sort_values("ticket_count", ascending=False)
        .to_dict(orient="records")
    )

    # 6. Business impact distribution
    patterns["business_impact"] = (
        df.groupby(["category", "business_impact"])
        .size()
        .reset_index(name="ticket_count")
        .sort_values("ticket_count", ascending=False)
        .to_dict(orient="records")
    )

    # 7. Urgency distribution
    patterns["urgency"] = (
        df.groupby(["category", "urgency"])
        .size()
        .reset_index(name="ticket_count")
        .sort_values("ticket_count", ascending=False)
        .to_dict(orient="records")
    )

    # 8. SLA breaches by category
    patterns["sla_breaches"] = (
        df.groupby(["category", "sla_breached"])
        .size()
        .reset_index(name="ticket_count")
        .sort_values("ticket_count", ascending=False)
        .to_dict(orient="records")
    )

    return {
        "total_tickets": len(df),
        "patterns": patterns
    }