from typing import Dict


def calculate_priority(
    customer_impact: str,
    business_impact: str,
    urgency: str,
    resolution_minutes: int,
    sla_target_minutes: int
) -> Dict:

    score = 0
    reasons = []

    # Customer impact
    if customer_impact.lower() == "high":
        score += 3
        reasons.append("High customer impact")
    elif customer_impact.lower() == "medium":
        score += 2
    else:
        score += 1

    # Business impact
    if business_impact.lower() == "high":
        score += 3
        reasons.append("High business impact")
    elif business_impact.lower() == "medium":
        score += 2
    else:
        score += 1

    # Urgency
    if urgency.lower() == "high":
        score += 3
        reasons.append("High urgency")
    elif urgency.lower() == "medium":
        score += 2
    else:
        score += 1

    # SLA risk
    if resolution_minutes > sla_target_minutes:
        score += 3
        reasons.append("SLA breached")
    elif resolution_minutes >= sla_target_minutes * 0.8:
        score += 2
        reasons.append("High SLA risk")
    else:
        score += 1

    # Priority mapping
    if score >= 10:
        priority = "P1"
    elif score >= 7:
        priority = "P2"
    elif score >= 5:
        priority = "P3"
    else:
        priority = "P4"

    return {
        "priority": priority,
        "score": score,
        "reason": ", ".join(reasons)
    }