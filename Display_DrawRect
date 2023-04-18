import time
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER, PEN_P8 #lib für Display

#Display instanzieren/initialisieren
display = PicoGraphics(display=DISPLAY_PICO_EXPLORER) 

# Konstante fürs Zeichnen
WIDTH, HEIGHT = display.get_bounds()

# Farben erstellen
BLACK = display.create_pen(0, 0, 0)
WHITE = display.create_pen(255, 255, 255)
GREEN = display.create_pen(0, 255, 0)

# Display löschen
display.set_pen(BLACK)
display.clear()
display.update()

# Arbeitsschleife
while 1:
    # Rechtecke immer größer und kleiner werden lassen:
    for i in range(WIDTH):
        display.set_pen(BLACK) # Display löschen
        display.clear()
        
        display.set_pen(GREEN) # mit Grün Zeichnen
        display.rectangle(1,1,i,i) # Rechteck (wird immer größer)
        display.update() 

    for i in range(WIDTH, 0, -2):
        display.set_pen(BLACK)
        display.clear()
        
        display.set_pen(GREEN)
        display.rectangle(1,1,i,i)
        display.update()
