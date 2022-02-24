import random
import sys


# Create a string with all uppercase characteres
uppercases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Create a string with all lowercase characteres
lowercases = "abcdefghijklmnopqrstuvwxyz"

# Create a string with all numbers
numbers = "0123456789"

# Create a string with the most used symbols
symbols = "!@#$%¨^&*()_+-=[]{}|\;':,./<>?`§£¢¬"


# Create a function that will generate a password
def generate_passoword(
    length, uppercase=True, lowercase=True, number=True, symbol=True
):
    """This function will generate a password with the given parameters

    Args:
        length (int): Length of the password
        uppercase (bool, optional): [If True, the password will have uppercase]. Defaults to True.
        lowercase (bool, optional): [If True, the password will have lowercase]. Defaults to True.
        number (bool, optional): [If True, the password will have numbers]. Defaults to True.
        symbol (bool, optional): [If True, the password will have symbols]. Defaults to True.

    Returns:
        [str|None]: [returns a string with the password generated or None if the parameters are wrong]
    """

    # Create a variable that will store the characters that will be used
    characteres = ""

    # If all parameters are False, show an message and return None
    if not uppercase and not lowercase and not symbol and not number:
        print("You must choose at least one type of charactere")
        return None

    if uppercase:
        characteres += uppercases
    if lowercase:
        characteres += lowercases
    if number:
        characteres += numbers
    if symbol:
        characteres += symbols

    # Create the password
    password = "".join(random.sample(characteres, length))

    return password


# Array that will store the parameters
options = []

# Get the length of the password from the command line, default is 8
try:
    length = sys.argv[1]
    if length.isdigit():
        length = int(length)
    else:
        raise TypeError("The length must be a number")
except IndexError or TypeError:
    print("Not enough parameters, using default length (8)")
    length = 8

# Get the parameters from the user
options.append(
    False if input("Do you want uppercase characteres? (y/n) ['y']: ") == "n" else True
)
options.append(
    False if input("Do you want lowercase characteres? (y/n) ['y']: ") == "n" else True
)
options.append(False if input("Do you want numbers? (y/n) ['y']: ") == "n" else True)
options.append(False if input("Do you want symbols? (y/n) ['y']: ") == "n" else True)
print()

passwd = generate_passoword(length, *options)
print(passwd) if passwd else sys.exit()

sys.exit()
