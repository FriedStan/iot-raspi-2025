import RPi.GPIO as GPIO
import time

KEYPAD = [
    [1, 2, 3, 'A'],
    [4, 5, 6, 'B'],
    [7, 8, 9, 'C'],
    ['*', 0, '#', 'D']
]

ROWS = [4, 17, 27, 22]
COLS = [5, 6, 13, 19]

GPIO.setmode(GPIO.BCM)

for row_pin in ROWS:
    GPIO.setup(row_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

for col_pin in COLS:
    GPIO.setup(col_pin, GPIO.OUT)
    GPIO.output(col_pin, GPIO.HIGH)

def get_key():
    key = None
    
    for col_num, col_pin in enumerate(COLS):
        GPIO.output(col_pin, GPIO.LOW)

        for row_num, row_pin in enumerate(ROWS):
            if GPIO.input(row_pin) == GPIO.LOW:
                key = KEYPAD[row_num][col_num]

                while GPIO.input(row_pin) == GPIO.LOW:
                    time.sleep(0.05)
        
        GPIO.output(col_pin, GPIO.HIGH)
    return key

try:
    while True:
        pressed_key = get_key()

        if pressed_key is not None:
            print(f"Presses: {pressed_key}")
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()