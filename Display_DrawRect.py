from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER, PEN_RGB565 #lib für Display

#Display instanzieren/initialisieren
display = PicoGraphics(display=DISPLAY_PICO_EXPLORER, pen_type=PEN_RGB565) 

# Konstante fürs Zeichnen
WIDTH, HEIGHT = display.get_bounds()

# Farben erstellen
BLACK = display.create_pen(0, 0, 0)
WHITE = display.create_pen(255, 255, 255)

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
        
        display.set_pen(display.create_pen(i,100,0)) # mit verändernder Farbe zeichnen
        display.rectangle(1,1,i,i) # Rechteck zeichnen (wird immer größer)
        display.update() # Ausgabe aufs Display

    for i in range(WIDTH, 0, -2):
        display.set_pen(BLACK)
        display.clear()
        
        display.set_pen(display.create_pen(i,100,0))
        display.rectangle(1,1,i,i)
        display.update()
