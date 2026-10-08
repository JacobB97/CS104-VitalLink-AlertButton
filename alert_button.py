import time
import requests
import RPi.GPIO as GPIO

BOT_TOKEN = "8825405607:AAE-k34lowIX7KtCwDCga8BRTRvikiq63Dg"
CHAT_ID = "8375057118"
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(7) == GPIO.HIGH:
        print("Someone pressed the alert button!")
        payload = {
            "chat_id": CHAT_ID,
            "text": "Someone pressed the alert button!"
        }
        requests.post(TELEGRAM_URL, data=payload)
        time.sleep(1)
    time.sleep(0.05)
