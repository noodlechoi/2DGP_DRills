from pico2d import *
from random import *

WIDTH, HEIGHT = 1280, 1024
open_canvas(WIDTH, HEIGHT)
ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')
cell_size = 64


def handle_events():
    global running, x, y, dir, frame

    events = get_events()
    for event in events:
        # 프로그램 종료
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, HEIGHT - 1 - event.y


def character_move():
    global x, y, dir, frame

    # 이동
    step = 10
    x += dir['x'] * step
    y += dir['y'] * step

    # 화면 밖으로 나가지 않게
    size = + cell_size / 2
    if (x <= 0 + size or x >= WIDTH - size or y <= 0 + size or y >= HEIGHT - size):
        x -= dir['x'] * step
        y -= dir['y'] * step

    # 움직을 때만 frame 움직이기
    if (dir['x'] != 0 or dir['y'] != 0):
        frame['x'] = (frame['x'] + 1) % 9


running = True
x = WIDTH // 2
y = HEIGHT // 2
frame = {'x': 0, 'y': 0}
dir = {'x': 0, 'y': 0}

while running:
    # 그리기
    clear_canvas()
    ground.draw(WIDTH // 2, HEIGHT // 2)
    hand.draw(x, y, cell_size, cell_size)
    character.clip_draw(frame['x'] * cell_size, frame['y'] * cell_size, cell_size, cell_size, x, y, cell_size * 2,
                        cell_size * 2)
    update_canvas()
    # 입력
    handle_events()
    character_move()

    delay(0.05)

close_canvas()


