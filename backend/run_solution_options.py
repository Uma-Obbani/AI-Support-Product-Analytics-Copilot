from app.solution_options import generate_solution_options


result = generate_solution_options("Payment")


print("\n===== SOLUTION OPTIONS =====")

print("\nProblem Area:")
print("→", result["problem_area"])

print("\nPossible Solutions:")

for option in result["options"]:
    print("\nOption:", option["option"])
    print("Type:", option["type"])
    print("Description:", option["description"])
    print("Status:", option["status"])