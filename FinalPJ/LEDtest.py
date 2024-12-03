import RPi.GPIO as GPIO
import time

# LED 핀 설정
LED_PINS = {'green': 17, 'red': 27}

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# LED 핀을 출력으로 설정
for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)

# LED 테스트
try:
    print("LED 테스트 시작! (3초 간격으로 켜지고 꺼짐)")
    while True:
        for color, pin in LED_PINS.items():
            print(f"{color} LED 켜짐")
            GPIO.output(pin, GPIO.HIGH)  # LED 켜기
            time.sleep(3)  # 3초 대기
            print(f"{color} LED 꺼짐")
            GPIO.output(pin, GPIO.LOW)  # LED 끄기
        time.sleep(1)  # 1초 대기 후 다음 LED로
except KeyboardInterrupt:
    print("테스트 종료!")
finally:
    GPIO.cleanup()
