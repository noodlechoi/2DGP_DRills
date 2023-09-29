from pico2d import *
from random import *

WIDTH, HEIGHT = 1280, 1024
open_canvas(WIDTH, HEIGHT)
ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')
cell_size = 64

def handle_events():
    global running, targets, mouse_x, mouse_y

    events = get_events()
    for event in events:
        # 프로그램 종료
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse_x , mouse_y = event.x, HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                target = event.x, HEIGHT - 1 - event.y
                targets.append(target)

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

# 그리기 함수
def draw_object():
    global targets, frame, mouse_y, mouse_y
    # 그리기
    clear_canvas()
    ground.draw(WIDTH // 2, HEIGHT // 2)
    hand.draw(mouse_x, mouse_y, cell_size, cell_size)
    for target in targets:
        hand.draw(target[0], target[1], cell_size, cell_size)
    character.clip_draw(frame['x'] * cell_size, frame['y'] * cell_size, cell_size, cell_size, x, y, cell_size * 2,
                        cell_size * 2)
    update_canvas()
    delay(0.1)

def move_line(target):
    global x, y

    # 프레임 계산 (y), (x, y) - target을 해서 그 값에 따라 방향 결정
    # x > 0 : left, x < 0 : right, y > 0 : down, y < 0 : up
    dir = [x - target[0], y - target[1]]
    # dirx 나 diry 중에서 절댓값이 더 큰 수를 기준으로 frame 이동
    if abs(dir[0]) > abs(dir[1]):
        if dir[0] > 0:
            frame['y'] = 2
        elif dir[0] < 0:
            frame['y'] = 0
    else:
        if dir[1] > 0:
            frame['y'] = 1
        elif dir[1] < 0:
            frame['y'] = 3

    for i in range(0, 100 + 1, 10):
        # 이동 계산
        t = i / 100
        x = (1-t)*x + t*target[0]
        y = (1-t)*y + t*target[1]

        frame['x'] = (frame['x'] + 1) % 9

        draw_object()




running = True
x = WIDTH // 2
y = HEIGHT // 2
mouse_x = 0
mouse_y = 0
frame = {'x': 0, 'y': 0}
dir = {'x': 0, 'y': 0}
targets = [(0, 0)]

hide_cursor()
while running:
    # 키입력
    handle_events()
    # 그리기
    for target in targets:
        move_line(target)
        # 끝까지 도착 시 리스트에서 제거
        targets.remove(target)

close_canvas()


