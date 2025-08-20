import smbus3
import time
# Get I2C bus
bus = smbus3.SMBus(1)
# SHT31 address, 0x44(68)
# Send measurement command, 0x2C(44)
# 0x06(06)High repeatability measurement
while True:
    bus.i2c_wr(0x44, [0x2C, 0x06])
    time.sleep(0.5)
    msg = bus.i2c_rd(0x44, 6)
    data = bytes(msg)
    bus.close
    temp = data[0] * 256 + data[1]
    cTemp = -45 + (175 * temp / 65535.0)
    humidity = 100 * (data[3] * 256 + data[4]) / 65535.0
    print("Temperature in Celsius is : %.2f C" % cTemp)
    print("Relative Humidity is : %.2f %%RH" % humidity)
    print("-----------------------------------")
    time.sleep(1)
