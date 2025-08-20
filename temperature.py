import time
import spidev
import RPi.GPIO as GPIO

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
ledpin = 12

GPIO.setup(ledpin, GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin, 1000)
pi_pwm.start(0)

def read_adc_ch0():
    cmd = [0b00000110, 0b00000000, 0b00000000]
    adc = spi.xfer2(cmd)
    result = ((adc[1] & 0b00001111) << 8) | adc[2]
    return result

try:
    while True:
        reading = read_adc_ch0()
        voltage = (reading * 3.3) / 4096
        temp = 100*(((reading*3.3)/4095)-1)+50
        print(f"Reading={reading}\t Voltage={voltage:.2f}\t Temp={temp:.2f}")
        time.sleep(0.1)

except KeyboardInterrupt:
    spi.close()
    print("\nSPI closed")