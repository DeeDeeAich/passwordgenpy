import random
import string
import sys

# Asking user for how many characters they want their password to be.
length = int(input("How many characters do you want your password to be? "))

# Checks if user's password length is longer than 24 characters, so that it doesn't overload a machine.
if(length > 24):
    print("You cannot have a password that long.")
    input("Press enter to exit...")
    sys.exit()

if(length < 4):
    print("You cannot have a password that short.")
    input("Press enter to exit...")
    sys.exit()

# Combining the strings of punctuation and ascii_letters so it's to randomly choose one character.
rand_characters = string.punctuation + string.ascii_letters

# Takes a random choice of the combined strings, punctuation and ascii_letters, a user defined amount of times and prints it out.
password = "".join(random.choice(rand_characters) for x in range(0, length))
print("Your randomly generated password is: " + password)
input("Press enter to exit...")