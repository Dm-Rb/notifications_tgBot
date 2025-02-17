import requests
"""
Этот модуль необходимо добавить в проект, 
далее импортировать функцию send_alert и вызвать send_alert() в месте события в проекте
"""
TOKEN = "your_bot_token"
CHAT_ID = 'your_user/chat_id'


def send_alert(text="Реп это кал!"):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    response = requests.post(url, json=payload)
    print(response.json())
