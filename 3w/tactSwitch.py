import RPi.GPIO as GPIO     

GPIO.setmode(GPIO.BCM)      # GPIO 핀들의 번호를 지정하는 규칙 설정


LED_pin = 2                     # LED 핀은 라즈베리파이 GPIO 2번핀으로 
sw_pin = 15                     # 스위치 핀은 라즈베리파이 GPIO 15번핀으로
GPIO.setup(LED_pin, GPIO.OUT)   # LED 핀을 출력으로 설정
GPIO.setup(sw_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)   
# 스위치 핀을 풀다운저항이 있는 출력으로 설정
# 풀다운 저항이 있으면 버튼을 누르지 않으면 LOW 신호가 됨
# 여기를 GPIO.PUD_UP으로 하면 버튼을 누르지 않으면 HIGH 신호가 됨


try:                                    # 이 try 안의 구문을 먼저 수행하고
    while True:                         
        if GPIO.input(sw_pin) == GPIO.HIGH:     # 스위치 핀이 HIGH이면 (버튼이 눌리면)
            GPIO.output(LED_pin, GPIO.HIGH)     # LED 핀을 HIGH로(LED 켬)
        else:                                   # 스위치 핀이 HIGH가 아니면 (버튼이 눌리지 않은 상태면)
            GPIO.output(LED_pin, GPIO.LOW)      # LED 핀을 LOW로(LED 끔)


finally:                                # try 구문이 종료되면
    GPIO.cleanup()                      # GPIO 핀들을 초기화
    
    
    
    
    