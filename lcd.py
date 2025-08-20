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
# แสดงข้อควำม
lcd.write_string("Hello, Raspberry")
lcd.crlf()  # ขึ ้นบรรทัดใหม่
lcd.write_string("I2C LCD Ready!")
time.sleep(5)
lcd.clear()  # ล้ำงหน้ำจอ  สดงข้อควำมใหม่
lcd.write_string("Line 1 Example")
lcd.crlf()
lcd.write_string("Temp: 25.5 C")

while True:
   num = random.randrange(1,10)
   if(num == 5):
      lcd.clear()
      lcd.write_string("(#^_^#)")
   elif(num == 1):
      lcd.clear()
      lcd.write_string("❤️ (•́ ω •̀๑)")
   else:
      lcd.clear()
      lcd.write_string("( *’ω’* )")
   time.sleep(1)
