import random
import sys


uppercases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercases = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%¨^&*()_+-=[]{}|\;':,./<>?`~²¹³ºª°\"§£¢¬'"


def generate_passoword(
    length, uppercase=True, lowercase=True, number=True, symbol=True
):
    characteres = ""

    if not uppercase and not lowercase and not symbol and not number:
        print("You must choose at least one type of charactere")
        return

    if uppercase:
        characteres += uppercases
    if lowercase:
        characteres += lowercases
    if number:
        characteres += numbers
    if symbol:
        characteres += symbols

    password = "".join(random.sample(characteres, length))

    return password

options = []
length = sys.argv[1]

try:
    length = int(length)
except ValueError:
    print("You must enter a number")
    sys.exit()

options.append(False if input("Do you want uppercase characteres? (y/n) ['y']: ") == "n" else True)
options.append(False if input("Do you want lowercase characteres? (y/n) ['y']: ") == "n" else True)
options.append(False if input("Do you want numbers? (y/n) ['y']: ") == "n" else True)
options.append(False if input("Do you want symbols? (y/n) ['y']: ") == "n" else True)
print()

print(generate_passoword(length, options[0], options[1], options[2], options[3]))
sys.exit()