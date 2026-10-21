def create_validation_summary(findings: list):
    """
    Summarize findings collected from Support, Product,
    Engineering and other relevant teams.
    """

    confirmed = []
    to_validate = []
    hypotheses = []

    for finding in findings:
        status = finding["status"].upper()

        if status == "CONFIRMED":
            confirmed.append(finding)

        elif status == "TO_VALIDATE":
            to_validate.append(finding)

        elif status == "HYPOTHESIS":
            hypotheses.append(finding)

    return {
        "confirmed_findings": confirmed,
        "findings_to_validate": to_validate,
        "hypotheses": hypotheses,
        "validation_complete": (
            len(to_validate) == 0
        )
    }