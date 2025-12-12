"""
    Purpose: This tool finds the age of the user

    Input: name and birth year
    Output: name and age

    Example:
    Input:
    John
    1999
    
    Output:
    Hello John, you are 26 years old.
"""
from datetime import datetime


def get_name():
    """
    Prompt the user for their name and validate the input.

    Returns:
        str: A cleaned, alphabetic name entered by the user.
    """
    while True:
        name = input("Enter your name: ")
        if name.isalpha():
            break
        elif name == '':
            print("You need to enter a name, you cannot leave it blank")
        elif name.isalnum():
            print("Please enter a valid name")
        else:
            print("please enter letters only")
    return name


def get_birth_year():
    """
    Prompt the user for their birth year and validate that it is a number.

    Returns:
        int: The birth year provided by the user.
    """
    while True:
        try:
            birth_year = int(input("Enter your birth year: "))
            if birth_year < 1900 or birth_year > 2025:
                print("Please enter a valid year between 1900 and 2025")
                continue
        except ValueError:
            print("You need to enter the year as digits")
        else:
            break
    return birth_year


def calculate_age(birth_year):
    """
    Calculate the user's age based on the current year.

    Args:
        birth_year (int): The user's year of birth.

    Returns:
        int: The user's age in full years.
    """
    current_year = datetime.now().year
    age = current_year - birth_year
    return age


def main():
    """
    Run the age calculator tool.

    Prompts the user for their name and birth year, calculates their age,
    and prints a formatted message to the console.
    """
    name = get_name()
    birth_year = get_birth_year()
    age = calculate_age(birth_year)
    print(f"Hello {name.capitalize()}, you are {age} years old.")


if __name__ == '__main__':
    main()
