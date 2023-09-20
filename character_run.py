from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print('CIRCLE')
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(400, 90)
    pass

def run_rectangle():
    print('RECTANGLE')
    pass

while True:
    # 함수 호출을 먼저씀
    run_circle()
    run_rectangle()

close_canvas()
