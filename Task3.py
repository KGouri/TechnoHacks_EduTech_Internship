import string
import random

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example: Generate a random password of length 12
password_length = int(input("Enter password length: "))
random_password = generate_random_password(password_length)
print(f"Random Password: {random_password}")
