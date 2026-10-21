def generate_solution_options(problem_area: str):
    options = []

    if problem_area.lower() == "payment":
        options = [
            {
                "option": "Improve payment error handling",
                "type": "Product",
                "description": (
                    "Improve the customer experience when a payment fails "
                    "by providing clearer error messages and next steps."
                ),
                "status": "OPTION"
            },
            {
                "option": "Investigate payment API failures",
                "type": "Technical",
                "description": (
                    "Investigate and address technical failures "
                    "in the payment integration."
                ),
                "status": "OPTION"
            },
            {
                "option": "Improve support-agent payment visibility",
                "type": "Product / Process",
                "description": (
                    "Provide support teams with better information "
                    "about payment status and failure reasons."
                ),
                "status": "OPTION"
            },
            {
                "option": "Automate payment-status investigation",
                "type": "Automation",
                "description": (
                    "Investigate whether payment-status checks "
                    "can be automated to reduce manual support work."
                ),
                "status": "OPTION"
            },
            {
                "option": "Improve payment support workflow",
                "type": "Process",
                "description": (
                    "Review and simplify the workflow used to "
                    "handle payment-related support cases."
                ),
                "status": "OPTION"
            }
        ]

    else:
        options = [
            {
                "option": "Investigate product improvement",
                "type": "Product",
                "description": (
                    f"Investigate potential product improvements "
                    f"for the {problem_area} problem."
                ),
                "status": "OPTION"
            },
            {
                "option": "Investigate technical causes",
                "type": "Technical",
                "description": (
                    f"Investigate potential technical causes "
                    f"of the {problem_area} problem."
                ),
                "status": "OPTION"
            },
            {
                "option": "Investigate process improvement",
                "type": "Process",
                "description": (
                    f"Investigate whether the {problem_area} "
                    "support process can be improved."
                ),
                "status": "OPTION"
            },
            {
                "option": "Investigate automation",
                "type": "Automation",
                "description": (
                    f"Investigate whether repetitive {problem_area} "
                    "activities could be automated."
                ),
                "status": "OPTION"
            }
        ]

    return {
        "problem_area": problem_area,
        "options": options
    }