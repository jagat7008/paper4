import random
import string

def generate_password(length):
    # Define character set
    char_set = string.ascii_letters + string.digits + string.punctuation

    # Generate sequence of characters
    password_chars = [random.choice(char_set) for _ in range(length)]

    # Combine characters into string
    password = ''.join(password_chars)

    return password
print(generate_password(100))