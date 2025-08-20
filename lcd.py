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
prev = 0
while True:
   num = random.randrange(1,10)
   if(num == 5 and prev != 5):
      lcd.clear()
      lcd.write_string("(#^_^#)")
   elif(num == 1 and prev != 1):
      lcd.clear()
      lcd.write_string("(>‿<)")
   elif(prev!=num):
      lcd.clear()
      lcd.write_string("(•ᴗ•)")
   prev = num
   time.sleep(1)
