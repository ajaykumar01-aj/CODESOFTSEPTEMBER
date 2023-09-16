# Password Generator
import random
import string

def generate_password(length):
    #define character sets for password complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    #combine character sets based on complexity
    if length < 4:
        character_set = lowercase_letters
    elif length < 8:
        character_set = lowercase_letters + digits
    elif length < 12:
        character_set = lowercase_letters + uppercase_letters + digits
    else:
        character_set = lowercase_letters + uppercase_letters + digits + special_characters

    # generate the password
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

#prompt the user for password length
try:
    length = int(input("Enter the desired length of the password: "))

    if length < 1:
        print("Password length should be atleast 1.")
    else:
        # generate and display the password
        password = generate_password(length)
        print("Generated Password: ", password)
except ValueError:
    print("Invalid input. Please enter a vaid integer for password length. ")
        
