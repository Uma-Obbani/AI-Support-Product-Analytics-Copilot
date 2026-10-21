def assess_business_impact(
    customer_impact,
    revenue_impact,
    conversion_impact,
    operational_cost,
    strategic_importance
):
    impacts = {
        "customer_impact": customer_impact,
        "revenue_impact": revenue_impact,
        "conversion_impact": conversion_impact,
        "operational_cost": operational_cost,
        "strategic_importance": strategic_importance
    }

    validated = []
    to_validate = []
    unavailable = []

    for area, value in impacts.items():

        if value is None:
            unavailable.append(area)

        elif isinstance(value, dict):
            status = value.get("status", "").upper()

            if status == "VALIDATED":
                validated.append({
                    "area": area,
                    "value": value
                })

            elif status == "TO_VALIDATE":
                to_validate.append({
                    "area": area,
                    "value": value
                })

            else:
                unavailable.append(area)

        else:
            to_validate.append({
                "area": area,
                "value": value
            })

    if to_validate:
        overall_status = "INCOMPLETE"

    elif validated:
        overall_status = "VALIDATED"

    else:
        overall_status = "NOT_VALIDATED"

    return {
        "overall_status": overall_status,
        "validated_impacts": validated,
        "impacts_to_validate": to_validate,
        "unavailable_impacts": unavailable
    }