import RPi.GPIO as GPIO
import time

KEYPAD = [
    [1, 2, 3, 'A'],
    [4, 5, 6, 'B'],
    [7, 8, 9, 'C'],
    ['*', 0, '#', 'D']
]

SEVEN_COLOR = [
    [0, 1, 1],
    [0, 0, 1],
    [1, 0, 1],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 0]
]

RED=2
GREEN=3
BLUE=4

ROWS = [23, 24, 25, 8]
COLS = [12, 16, 20, 21]

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED,GPIO.OUT)
GPIO.setup(BLUE,GPIO.OUT)
GPIO.setup(GREEN,GPIO.OUT)

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

        if pressed_key is not None and pressed_key in range(1, 8):
            print(f"Pressed: {pressed_key}")
            for count, color in enumerate(SEVEN_COLOR):
                if (pressed_key == count):
                    GPIO.output(GREEN,color[0])
                    GPIO.output(BLUE,color[1])
                    GPIO.output(RED,color[2])
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()