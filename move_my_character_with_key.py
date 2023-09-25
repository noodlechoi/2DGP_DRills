from pico2d import *

WIDTH, HEIGHT = 1280, 1024
open_canvas(WIDTH, HEIGHT)
ground = load_image('TUK_GROUND.png')
character = load_image('skell.png')
cell_size = 64

running = True

while running:
    clear_canvas()
    ground.draw(WIDTH // 2, HEIGHT // 2)
    character.clip_draw(0, 0, cell_size, cell_size, WIDTH // 2, HEIGHT // 2)
    update_canvas()
    delay(0.01)

close_canvas()