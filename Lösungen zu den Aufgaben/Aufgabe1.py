from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER, PEN_P8 #lib für Display

#Display instanzieren/initialisieren
display = PicoGraphics(display=DISPLAY_PICO_EXPLORER, pen_type=PEN_P8) 

# Konstante fürs Zeichnen
WIDTH, HEIGHT = display.get_bounds()

# Farben erstellen
BLACK = display.create_pen(0, 0, 0)
YEllOW = display.create_pen(255, 255, 0)
RED = display.create_pen(255, 0, 0)

# Display löschen
display.set_pen(BLACK)
display.clear()
display.update()

# Kreis und Linie Zeichnen
display.set_pen(YEllOW)
display.circle(int(WIDTH/2), int(HEIGHT/2), 50)
display.set_pen(RED)
display.line(0,int(HEIGHT/2+50),WIDTH,int(HEIGHT/2+50), 10)
display.update()