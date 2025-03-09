import requests
import time

BASE_URL = "http://backend:8080/api/feedback"

XSS_PAYLOADS = [
    '<script>alert("XSS 1")</script>',
    '<img src="x" onerror="alert(\'XSS 2\')">',
    '<svg/onload=alert("XSS 3")>',
    '<iframe src="javascript:alert(\'XSS 4\')"></iframe>',
    '<a href="javascript:alert(\'XSS 5\')">Click me</a>',
    "<body onload=alert('XSS 6')>",
    "<input type='text' value='XSS' onfocus='alert(\"XSS 7\")'>",
    "<div onmouseover='alert(\"XSS 8\")'>Hover me</div>",
    "<form action='javascript:alert(\"XSS 9\")'><input type='submit'></form>",
    "<math><mi><a xlink:href='javascript:alert(\"XSS 10\")'>Click</a></mi></math>"
]

def test_xss():
    print("\n[🔍] Running XSS Exploitation Test...\n")

    for i, payload in enumerate(XSS_PAYLOADS, start=1):
        data = {"name": f"Hacker_{i}", "message": payload}
        response = requests.post(f"{BASE_URL}/submit", json=data)

        if response.status_code == 200:
            print(f"[✔] Payload {i} injected successfully: {payload}")
        else:
            print(f"[✖] Payload {i} failed!")

        # time.sleep(1)  # Pauză mică între request-uri

    # 📌 Verificăm dacă payload-urile XSS au fost salvate și returnate de server
    print("\n[🔍] Checking if XSS payloads were stored...\n")
    feedbacks = requests.get(f"{BASE_URL}/list").json()

    for feedback in feedbacks:
        for payload in XSS_PAYLOADS:
            if payload in feedback["message"]:
                print(f"[⚠] Stored XSS Found in: {feedback['message']}")

    print("\n✅ XSS Test Completed!")

if __name__ == "__main__":
    test_xss()
