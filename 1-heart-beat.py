# Exploiter L'affichage LED
# Gérer la création d'image et leur affichage

import microbit as m
import time

tabImg=[      #SStocke les images de coeur
        m.Image("09090:" "99999:" "99999:" "09990:" "00900"),   # gros coeur
        m.Image("00000:" "09090:" "09990:" "00900:" "00000")    # petit coeur
        ]

while True:
    m.display.show(tabImg[0])
    m.sleep(500)
    m.display.show(tabImg[1])
    m.sleep(500)