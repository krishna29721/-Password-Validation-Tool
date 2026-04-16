import string

def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak "
    elif score == 3 or score == 4:
        return "Medium "
    else:
        return "Strong "


def validate_password(password):
    try:
        if len(password) < 8:
            return "Password must be at least 8 characters"

        if not any(c.isupper() for c in password):
            return "Add at least one uppercase letter"

        if not any(c.islower() for c in password):
            return "Add at least one lowercase letter"

        if not any(c.isdigit() for c in password):
            return "Add at least one digit"

        if not any(c in string.punctuation for c in password):
            return "Add at least one special character"

        return "Valid Password "

    except Exception:
        return "Invalid Input"


# Main Program
while True:
    password = input("\nEnter Password: ")

    result = validate_password(password)
    print("Validation:", result)

    if result == "Valid Password ":
        strength = check_strength(password)
        print("Strength:", strength)

    choice = input("Try again? (y/n): ")
    if choice.lower() != 'y':
        print("Program Ended")
        break