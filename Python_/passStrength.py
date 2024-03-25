import string
import getpass


def check_password_strength():
    password = getpass.getpass("Enter your password: ")
    password_strength = 0
    remarks = ""
    lower_count = upper_count = digit_count = special_count = wspace_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            digit_count += 1
        elif char == " ":  # whitespace means simple space
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        password_strength += 1
    if upper_count >= 1:
        password_strength += 1
    if digit_count >= 1:
        password_strength += 1
    if special_count >= 1:
        password_strength += 1
    if wspace_count >= 1:
        password_strength += 1

    if password_strength == 1:
        remarks = "Password is very weak. Change it ASAP!"
    elif password_strength == 2:
        remarks = "Password is weak. Consider changing it."
    elif password_strength == 3:
        remarks = "Password is moderate. It's good."
    elif password_strength == 4:
        remarks = "Password is strong. Good to go!"
    elif password_strength == 5:
        remarks = "Password is very strong. Excellent!"

    print("Your password has:-")
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{digit_count} digits")
    print(f"{special_count} special characters")
    print(f"{wspace_count} whitespaces")
    print(f"Password Score: {password_strength}/5")
    print(f"Remarks: {remarks}")


def check_pwd(another_pw=False):
    valid = False
    if another_pw:
        choice = input(
            "Do you want to check another password's strength? (y/n): ")
    else:
        choice = input(
            "Do you want to check your password's strength? (y/n): ")

    while not valid:
        if choice.lower() == "y":
            return True
        elif choice.lower() == "n":
            print("Thank you for using this program. \nExiting...")
            return False
        else:
            print("Invalid choice! Please enter 'y' or 'n'.")


if __name__ == "__main__":
    print("\n\t\t=====Welcome to Exclusive Password Strength Checker=====\n")
    check_pw = check_pwd()
    while check_pw:
        check_password_strength()
        check_pw = check_pwd(True)