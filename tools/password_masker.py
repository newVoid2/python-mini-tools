"""
    Purpose: This tools is to state the username and the hidden form of the password and it length back to the user to hide sensitive input.

    Input: username + password
    Output: username + masked password + length of password

    Example:
    Input: 
    What is your username? John
    What is your password? secret

    Output:
    John, your password ****** is 6 characters long.
"""

def masked_password(length_of_password):
    """Create the hidden password form"""
    return '*' * length_of_password

def main():
    username = input("What is your username? ")
    password = input("What is your password? ")
    while True:
        if username == '':
            username = input("What is your username? ")
        elif password == '':
            password = input("What is your password? ")
        elif username != '' and password != '':
            break
    length_of_password = len(password)
    hidden_password = masked_password(length_of_password)
    print(f"{username}, your password {hidden_password} is {length_of_password} characters long.")

if __name__ == '__main__':
    main()