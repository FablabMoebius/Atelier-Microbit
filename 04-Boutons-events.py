# Utilisation des boutons et gestion des évènements

# Importations
import microbit as m

# Initialisations
tabImg=[      #Stocke les images
        m.Image("00000:" "00000:" "00000:" "00000:" "00000"),   # 0. vide
        m.Image("09090:" "99999:" "99999:" "09990:" "00900"),   # 1. gros coeur
        m.Image("00000:" "09090:" "09990:" "00900:" "00000"),   # 2. petit coeur
        m.Image("00000:" "00000:" "00900:" "00000:" "00000"),   # 3. petit carré
        m.Image("00000:" "09990:" "09990:" "09990:" "00000")    # 4. gd carré
        ]
boutonA = m.button_a
boutonB = m.button_b

# Fonction d'affichage d'un coeur qui bat
def coeur():
    m.display.show(tabImg[1])
    m.sleep(200)
    m.display.show(tabImg[2])
    m.sleep(200)

# Fonction d'affichage d'un carré qui bat
def carre():
    m.display.show(tabImg[3])
    m.sleep(200)
    m.display.show(tabImg[4])
    m.sleep(200)

while True:
        if boutonA.is_pressed() == 1 :   
            coeur()
        elif boutonB.is_pressed() == 1 :
            carre()
        else:
            m.display.show(tabImg[0]) # Affichage d'une image vide