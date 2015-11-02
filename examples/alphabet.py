#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pcd8544.lcd as lcd
import time, os, sys

if not os.geteuid() == 0:
    sys.exit('Script must be run as root')

ON, OFF = [1, 0]

try:
    lcd.init()
    lcd.cls()
    lcd.set_brightness(500)
    lcd.backlight(ON)
    for i in range(32, 116):
        lcd.display_char(chr(i))
    time.sleep(10)
except KeyboardInterrupt:
  pass
finally:
  lcd.cls()
  lcd.backlight(OFF)

