import time
import spidev
import math
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 44444


def ReadChannel(channel):
    adc = spi.xfer2([6 | (channel & 4) >> 2, (channel & 3) << 6, 0])
    data = ((adc[1] & 15) << 8) + adc[2]
    return data

track = "/"

try:
    while True:
        reading_mpc = ReadChannel(0)
        reading_thermistor = ReadChannel(6)
        voltage_mpc = (reading_mpc * 3.3) / 4096
        temp_mpc = 100*(((reading_mpc*3.3)/4096)-1)+50

        voltage_thermistor = (reading_thermistor * 3.3) / 4096
        r_thermistor = (10000 * voltage_thermistor) / (3.3 - voltage_thermistor)
        temp_thermistor = (1/((1/(25+273.15))+(1/4050)*math.log(r_thermistor/10000))) - 270.5
        print(f"Temp_mpc={temp_mpc:.2f}\t Temp_therm={temp_thermistor:.2f} {track} {reading_thermistor} {r_thermistor}")
        if track == "/":
            track="\\"
        else:
            track="/"
        time.sleep(0.3)

except KeyboardInterrupt:
    spi.close()
    print("\nSPI closed")