from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')



x = 400
y = 90

rec = True
while True:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    if rec:
        if( x >= 780 and y <= 550):
            y = y + 2
        elif y >= 540 and x >= 30:
            x = x - 2
        elif x <= 30 and y >= 90:
            y = y - 2
        elif y <= 90:
            y = 90
            x += 2
            if(x >= 380 and x <= 400 and y == 90):
                rec = False
    else:
        x = math.cos(270 / 360 * 2 * math.pi)
        y = y + math.sin(270 / 360 * 2 * math.pi)
        if(x >= 380 and x <= 400 and y == 90):
                rec = True
    delay(0.01)
    



close_canvas()
