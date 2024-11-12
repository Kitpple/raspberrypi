import RPi.GPIO as GPIO
import time
import random

# GPIO 설정
GPIO.setmode(GPIO.BCM)

# LED와 버튼 핀 설정
LED_PINS = {'red':2, 'green': 10}
BUTTON_PINS = {'red': 17, 'green': 18}

# LED와 버튼 핀 초기화
for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)
for pin in BUTTON_PINS.values():
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# 변수 설정
n_trials = 5  # 사용자가 연속으로 성공해야 하는 횟수
max_fails = 3  # 게임 자동 종료 전 최대 실패 횟수
reaction_time_limit = 3  # LED 켜진 상태로 반응을 기다리는 시간 (초)

# 게임 상태 변수
total_score = 0
successful_trials = 0
fail_count = 0

def light_random_led():
    color = random.choice(list(LED_PINS.keys()))
    GPIO.output(LED_PINS[color], GPIO.HIGH)
    return color

def clear_leds():
    for pin in LED_PINS.values():
        GPIO.output(pin, GPIO.LOW)

def reset_signal():
    for pin in LED_PINS.values():
        GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    clear_leds()

try:
    while True:
        if fail_count >= max_fails:
            print("실격 처리되었습니다! 총 점수:", total_score)
            break

        clear_leds()
        color_to_press = light_random_led()
        start_time = time.time()
        pressed = False

        while time.time() - start_time < reaction_time_limit:
            if GPIO.input(BUTTON_PINS[color_to_press]) == GPIO.HIGH:
                reaction_time = time.time() - start_time
                total_score += reaction_time
                print(f"{color_to_press} 버튼을 {reaction_time:.2f}초 만에 누름")
                successful_trials += 1
                pressed = True
                break

        clear_leds()

        if not pressed:
            fail_count += 1
            successful_trials = 0
            reset_signal()
            print("실패했습니다. 처음부터 다시 시작하세요.")

        if successful_trials == n_trials:
            print("축하합니다! 게임 종료. 최종 점수:", total_score)
            break

finally:
    clear_leds()
    GPIO.cleanup()
