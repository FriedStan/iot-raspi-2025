from RPLCD.i2c import CharLCD
import time
import random
# สร้ำงออบเจ็กต์ LCD
lcd = CharLCD(
    i2c_expander='PCF8574',
    address=0x27,
    port=1,
    cols=16,
    rows=2,
    charmap='A00',
    auto_linebreaks=True,
    backlight_enabled=True
)
while True:
   lcd.write_string("本")
   time.sleep(1)
