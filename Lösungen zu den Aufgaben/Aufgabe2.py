from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER, PEN_P8 #lib für Display
import time
from machine import Pin

# Display instanzieren/initialisieren
display = PicoGraphics(display=DISPLAY_PICO_EXPLORER, pen_type=PEN_P8) 

# Konstante fürs Zeichnen
WIDTH, HEIGHT = display.get_bounds()

# Taster definieren
tasterA=Pin(12, Pin.IN, Pin.PULL_UP)
tasterB=Pin(13, Pin.IN, Pin.PULL_UP)

# Farben erstellen
BLACK = display.create_pen(0, 0, 0)
YELLOW = display.create_pen(255, 255, 0)
RED = display.create_pen(255, 0, 0)

# Display löschen
display.set_pen(BLACK)
display.clear()
display.update()

# Variablen für Stoppuhr
start = 0
stop = 0
stopped = True

# Klassische Schriftart
display.set_font("bitmap8")

# Arbeitsschleufe
while True:
    # Taster A gedrückt: Stoppuhr wird gestartet
    if tasterA.value() == 0:
        start = time.ticks_ms()
        stopped = False
    
    # Taster B gedrückt: Stoppuhr wird gestoppt
    if tasterB.value() == 0:
        stop = time.ticks_ms()
        stopped = True
    
    # Display löschen
    display.set_pen(BLACK)
    display.clear()
    
    # Ausgabe auf Display
    display.set_pen(RED)

    if stopped == True:
        display.text(str((stop-start)/1000)+"s", int(WIDTH/2)-65, int(HEIGHT/2)-20, scale=5)
    else:
        display.text(str((time.ticks_ms()-start)/1000)+"s", int(WIDTH/2)-65, int(HEIGHT/2)-20, scale=5)
        
    display.update()
