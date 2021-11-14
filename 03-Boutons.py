# Utilisation des boutons

# Importations
import microbit as m

# Initialisations
tabImg=[      #SStocke les images de coeur
        m.Image("09090:" "99999:" "99999:" "09990:" "00900"),   # 0. gros coeur
        m.Image("00000:" "09090:" "09990:" "00900:" "00000"),   # 1. petit coeur
        m.Image("00000:" "00000:" "00900:" "00000:" "00000"),   # 2. petit carré
        m.Image("00000:" "09990:" "09990:" "09990:" "00000")    # 3. gd carré
        ]
boutonA = m.button_a

while True:
        if boutonA.is_pressed() ==1 :   
                m.display.show(tabImg[0])
                m.sleep(500)
                m.display.show(tabImg[1])
                m.sleep(500)
        else:
                m.display.show(tabImg[2])
                m.sleep(500)
                m.display.show(tabImg[3])
                m.sleep(500)