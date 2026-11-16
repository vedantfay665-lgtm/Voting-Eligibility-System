def check_eligibility(name, age, citizen):
    """Returns (eligible: bool, message lines: list)."""
    if age >= 18 and citizen == "y":
        return True, [f"{name} is eligible to vote."]
    elif age < 18 and citizen == "y":
        return False, [f"{name} is not eligible to vote.",
                       f"Years left to become eligible: {18 - age}"]
    elif age >= 18 and citizen == "n":
        return False, [f"{name} is not eligible to vote.",
                       "Reason: Not an Indian citizen."]
    else:
        return False, [f"{name} is not eligible to vote.",
                       "Reason: Not an Indian citizen.",
                       f"Years left to become eligible: {18 - age}"]


def get_age():
    while True:
        try:
            age = int(input("Age: "))
        except ValueError:
            print("Invalid input. Enter a whole number.")
            continue
        if age < 0 or age > 120:
            print("Invalid age. Age must be between 0 and 120.")
            continue
        return age


def get_citizen():
    while True:
        c = input("Indian citizen (y/n): ").strip().lower()
        if c in ("y", "n"):
            return c
        print("Please enter y or n.")


def main():
    checked = eligible = not_eligible = 0
    while True:
        name = input("Name: ").strip()
        age = get_age()
        citizen = get_citizen()

        ok, lines = check_eligibility(name, age, citizen)
        for line in lines:
            print(line)

        checked += 1
        if ok:
            eligible += 1
        else:
            not_eligible += 1

        again = input("Check another voter? (y/n): ").strip().lower()
        if again != "y":
            break

    print(f"Voters checked: {checked} | Eligible: {eligible} | Not eligible: {not_eligible}")


main()


