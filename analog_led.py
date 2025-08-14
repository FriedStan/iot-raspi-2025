import time
import RPi.GPIO as GPIO
import spidev
spi = spidev.SpiDev()
spi.open(0, 0)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
ledpin = 12

GPIO.setup(ledpin, GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin, 1000)
pi_pwm.start(0)

def ReadChannel(channel):
    adc = spi.xfer2([6 | (channel & 4) >> 2, (channel & 3) << 6, 0])
    data = ((adc[1] & 15) << 8) + adc[2]
    return data

while True:
    for i in range(8):
        reading = ReadChannel(0)
        voltage = (reading * 3.3) / 4096
        print(f"Reading={reading}\t Voltage={voltage}")
        pi_pwm.ChangeDutyCycle(reading / 4096 * 100)
        time.sleep(1)