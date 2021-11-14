# Attention le HP doit être branché sur pin0 et gnd
import microbit as m
import music


# Tune: Frere Jacques
tune = ["C4:4", "D4:4", "E4:4", "C4:4", "C4:4", "D4:4", "E4:4", "C4:4",
        "E4:4", "F4:4", "G4:8", "E4:4", "F4:4", "G4:8"]
while True:
    music.play(tune)
    m.sleep(2000)
    