import RPi.GPIO as GPIO
import time

# GPIO 모드 설정
GPIO.setmode(GPIO.BCM)

# 버튼 핀 번호
BUTTON_PINS = {'red': 17, 'green': 18}

# 버튼 핀 설정 (풀다운 저항 적용)
for pin in BUTTON_PINS.values():
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("버튼 테스트 시작! 버튼을 눌러보세요. 😊")

try:
    while True:
        # 빨강 버튼 테스트
        if GPIO.input(BUTTON_PINS['red']) == GPIO.HIGH:
            print("빨강 버튼 눌림!")
            time.sleep(0.3)  # 중복 출력 방지를 위해 약간의 지연 추가

        # 노랑 버튼 테스트
        if GPIO.input(BUTTON_PINS['green']) == GPIO.HIGH:
            print("초록 버튼 눌림!")
            time.sleep(0.3)  # 중복 출력 방지를 위해 약간의 지연 추가

finally:
    GPIO.cleanup()
    print("테스트 종료. GPIO 설정 초기화 완료.")
