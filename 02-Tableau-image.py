# Exploiter L'affichage LED
# Gérer la création d'image et leur affichage

import microbit as m

tabImg=[      #Stocke les images
        m.Image("00000:" "00000:" "00000:" "00000:" "00000"),   # 0. vide
        m.Image("09090:" "99999:" "99999:" "09990:" "00900"),   # 1. gros coeur
        m.Image("00000:" "09090:" "09990:" "00900:" "00000")   # 2. petit coeur
        ]


while True:
    m.display.show(tabImg[1]) # image issue de la bibliothèque
    m.sleep(500)
    m.display.show(tabImg[2])
    m.sleep(500)
