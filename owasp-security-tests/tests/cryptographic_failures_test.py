import requests
import hashlib
from itertools import product

# 🔗 Backend URL unde este endpoint-ul vulnerabil
BASE_URL = "http://backend:8080/api/cf/register"

# 🔑 Usernames (poți adăuga alții)
USERNAMES = ["lorinspan"]

# 🔐 Liste de parole comune (se poate extinde)
PASSWORDS = [
    "password", "password123", "parolasecreta"
]

# 📌 Hash-ul returnat de backend pentru "parolasecreta" (în format hex)
TARGET_HASH = "fac0ca33fa0b047f25b1b8b894dee2d6"

# 🕵️ Funcție pentru testarea atacului Rainbow Table (folosind parola hash-uită)
def test_rainbow_attack():
    print("[⚡] Încep testul de atac Rainbow Table...")
    found = False

    for password in PASSWORDS:
        md5_hash = hashlib.md5(password.encode()).hexdigest()  # Convertim corect în hex

        if md5_hash == TARGET_HASH:
            print(f"[✔] Crack reușit: {password} → {md5_hash}")
            found = True
            break  # Oprim căutarea dacă am găsit o potrivire

    # ✅ Înlocuim return found cu assert
    assert found, "[❌] Rainbow Table Attack a eșuat. Nu s-au găsit potriviri."