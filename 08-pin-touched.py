from microbit import *

while True:
    if pin0.is_touched():
        display.show(Image.HAPPY)
    if pin1.is_touched():
        display.show(Image.SAD)

    if button_a.is_pressed():
        display.show(Image.HAPPY)
    if button_b.is_pressed():
        display.show(Image.SAD)