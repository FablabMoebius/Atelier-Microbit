import microbit as m

# get_presses : compte les pressions
# Le microbit va "dormir" pendant 10s. Pendant ce laps de temps,
# il peut compter le nombre de pressions sur le bouton A
m.display.scroll("Start")
m.sleep(10000)
count = str(m.button_a.get_presses())
m.display.scroll("Nombre de pressions :")
m.display.show(count)
m.display.scroll("Fin")