from machine import Pin,I2C,RTC
from ssd1306 import SSD1306_I2C
i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c, 0x3c)
from time import sleep

rtc = RTC()

#(year, month, day, weekday, hours, minutes, seconds, subseconds)
rtc.datetime((2023, 2, 2, 4,13,55, 0,0)) 

while True:
    horloge=rtc.datetime()
    print(horloge)
    oled.fill(0)
    oled.text(str(horloge[4:7]), 0, 0)
    oled.show()
    sleep(1)
 