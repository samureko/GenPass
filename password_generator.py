import random
import string
import pyperclip

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":

    while True:
        password_length = int(input("Enter password length (default 12): ") or 12)
        generated_password = generate_password(password_length)
        pyperclip.copy(generated_password)

        print(f"Generated password: {generated_password}\n")
