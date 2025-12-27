"""Lead Pre-Qualification (CLI)

A simple command-line program that simulates a lead pre-qualification flow.
It collects basic information, confirms it with the user, classifies the lead,
and prints the next-step message for a sales representative.

Concepts used:
- Functions
- Dictionaries
- Conditionals
- Loops
- try/except input validation
"""

MINIMUM_AGE = 19
BASIC_INCOME_THRESHOLD = 3000


def collect_lead():
    """Collect lead data from the user.

    Returns:
        dict | None: lead dictionary on success, or None if invalid input.
    """
    name = input("Please enter your name: ").strip()
    if name == "":
        return None

    try:
        age = int(input("Please enter your age: "))
        monthly_income = float(input("Please enter your monthly income: "))
    except:
        return None

    if age <= 0:
        return None

    if monthly_income <= 0:
        return None

    return {
        "name": name,
        "age": age,
        "monthly_income": monthly_income
    }


def is_info_correct(lead):
    """Ask the user to confirm their information.

    Args:
        lead (dict): lead data

    Returns:
        bool: True if user confirms, otherwise False.
    """
    print(
        f"Your name is {lead['name']}, "
        f"your age is {lead['age']}, "
        f"and your monthly income is {lead['monthly_income']}."
    )

    answer = input("Is your info correct (Y/N)? ").upper()
    return answer == "Y"


def classify_lead(lead):
    """Classify a lead based on simple business rules."""
    if lead["age"] < MINIMUM_AGE:
        return "invalid"

    if lead["monthly_income"] < BASIC_INCOME_THRESHOLD:
        return "basic"

    return "qualified"


def generate_message(status):
    """Generate a message for the user based on lead status."""
    if status == "basic":
        return (
            "Thanks! A representative will review your info and "
            "assist you as soon as possible."
        )
    return "Great news! A representative will assist you shortly."


def run():
    """Run the CLI program."""
    while True:
        lead = collect_lead()
        if lead is None:
            print("Invalid information. Please try again.")
            continue

        if not is_info_correct(lead):
            print("Ok! Let's try again.")
            continue

        status = classify_lead(lead)

        if status == "invalid":
            print("Unfortunately, you are not eligible at this moment.")
        else:
            print(generate_message(status))

        break


if __name__ == "__main__":
    run()
