import time
import requests
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_pressed = False

while True:
    if GPIO.input(7) == GPIO.HIGH and not button_pressed:
        print("Someone pressed the alert button!")
        requests.post("https://api.telegram.org/bot8825405607:AAE-k34lowIX7KtCwDCga8BRTRvikiq63Dg/sendMessage", data={"chat_id": "8375057118", "text": "Someone pressed the alert button!"})
        button_pressed = True
    elif GPIO.input(7) == GPIO.LOW:
        button_pressed = False
    time.sleep(0.1)
