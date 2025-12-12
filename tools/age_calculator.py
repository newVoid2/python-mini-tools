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
    while True:
        name = input("Enter your name: ")
        if name.isalpha():
            break
        elif name == '':
            print("You need to enter a name, you cannot leave it blank")
        elif name.isalnum():
            print("Please enter a valid name")
    return name


def get_birth_year():
    while True:
        try:
            birth_year = int(input("Enter your birth year: "))
        except ValueError:
            print("You need to enter the year as digits")
        else:
            break
    return birth_year


def calculate_age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    return age


def main():
    name = get_name()
    birth_year = get_birth_year()
    age = calculate_age(birth_year)
    print(f"Hello {name.capitalize()}, you are {age} years old.")


if __name__ == '__main__':
    main()
