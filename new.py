import time
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

def read_adc_ch0():
    cmd = [0b00000110, 0b00000000, 0b00000000]
    adc = spi.xfer2(cmd)
    result = ((adc[1] & 0b00001111) << 8) | adc[2]
    return result

try:
    while True:
        value = read_adc_ch0()
        voltage = (value * 3.3) / 4096
        print(f"CH0: {value:4d} | {voltage:.2f} V")
        time.sleep(0.05)

except KeyboardInterrupt:
    spi.close()
    print("\nSPI closed")