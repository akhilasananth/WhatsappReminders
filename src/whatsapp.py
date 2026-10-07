import requests
from config import WHATSAPP_API_KEY, WHATSAPP_API_URL

def send_whatsapp_message(to, body):
    url = f"{WHATSAPP_API_URL}/messages/text"

    payload = {
        "typing_time": 0,
        "to": to,
        "body": body
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {WHATSAPP_API_KEY}"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 200:
        print(f"ERROR: Failed to send message. Response: {response.text}")
    
    print(f"INFO: Message sent successfully: {response.text}")

    return response.text
