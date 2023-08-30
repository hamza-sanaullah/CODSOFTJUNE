import random

def password(length):
    upper = input("Do you want upper case letters in your password (Y/N):").lower()
    lower = input("Do you want lower case letters in your password (Y/N):").lower()
    special_characters = input("Do you want special characters in your password (Y/N):").lower()
    digit = input("Do you want digits in your password (Y/N):").lower()

    all_characters = ""
    if upper == "y":
        all_characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if lower == "y":
        all_characters += "abcdefghijklmnopqrstuvwxyz"
    if digit == "y":
        all_characters += "0123456789"
    if special_characters == 'y':
        all_characters += "!@#$%^&*()<>?{}|`~"

    password = ""
    for i in range(length):
        password += random.choice(all_characters)
    return password

length = int(input("Please enter the length of the password:"))
generated_password = password(length)
print("Generated Password:", generated_password)

def strength(password):
    uppercase_present = any(char.isupper() for char in password)
    lowercase_present = any(char.islower() for char in password)

    if uppercase_present and lowercase_present:
        return "strong"
    else:
        return "weak"

password_strength = strength(generated_password)
print("Password Strength:", password_strength)

def count_characters(password, characters):
    count = sum(1 for char in password if char in characters)
    return count

uppercase_count = count_characters(generated_password, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(f"Number of uppercase letters: {uppercase_count}")

lowercase_count = count_characters(generated_password, "abcdefghijklmnopqrstuvwxyz")
print(f"Number of lowercase letters: {lowercase_count}")


