import base64
import random
import string

def generate_password(length=9):  
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def encrypt_base64(text, rounds=3):
    for _ in range(rounds):
        text = base64.b64encode(text.encode()).decode()
    return text

passwords = [generate_password() for _ in range(99)]  
passwords.append("chocolate") 

random.shuffle(passwords) 

encrypted_passwords = [encrypt_base64(pw) for pw in passwords]

with open("password.txt", "w") as file:
    for encrypted in encrypted_passwords:
        file.write(f"{encrypted}\n")
