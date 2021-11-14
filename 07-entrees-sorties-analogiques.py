# Lecture des valeurs d'un potentiometre
import microbit as m

while True:
    lecture = m.pin1.read_analog() # valeur entre 0 et 1023 où 0 = 0V et 1023 =3.3V
    m.sleep(200)
    pourcentage = lecture/1023*100
    pourcentage = round(pourcentage, 1)
    print(str(pourcentage)+" %")
    m.pin0.write_analog(lecture)
