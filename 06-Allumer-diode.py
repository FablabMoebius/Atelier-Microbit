import microbit as m #importe la librairie concernant le micro:bit

monBouton = m.button_a
pinSortie = m.pin0

while True:
    if monBouton.is_pressed() == 1:
        if pinSortie.read_digital() == 1:
            pinSortie.write_digital(0)
        else:
            pinSortie.write_digital(1)
        m.sleep(.5)
    m.sleep(200)