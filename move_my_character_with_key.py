from pico2d import *

WIDTH, HEIGHT = 1280, 1024
open_canvas(WIDTH, HEIGHT)
ground = load_image('TUK_GROUND.png')
character = load_image('skell.png')
cell_size = 64

def handle_events():
    pass

running = True
x = WIDTH // 2
y = HEIGHT // 2
frame = {'x' : 0, 'y' : 0}
dir = {'x' : 0, 'y' : 0}

while running:
    # 그리기
    clear_canvas()
    ground.draw(WIDTH // 2, HEIGHT // 2)
    character.clip_draw(frame['x'] * cell_size, frame['y'] * cell_size, cell_size, cell_size, x, y)
    update_canvas()
    # 입력
    handle_events()
    # 이동
    x += dir['x'] * 5
    y += dir['y'] * 5

    if(dir['x'] != 0 or dir['y'] != 0):
        frame['x'] = (frame['x'] + 1) % 9
    
    delay(0.05)

close_canvas()