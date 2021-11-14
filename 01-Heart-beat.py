# Exploiter L'affichage LED
# Gérer la création d'image et leur affichage

import microbit as m


while True:
    m.display.show(m.Image.PACMAN) # image issue de la bibliothèque
    m.sleep(500)
    m.display.show(m.Image.DUCK)
    m.sleep(500)