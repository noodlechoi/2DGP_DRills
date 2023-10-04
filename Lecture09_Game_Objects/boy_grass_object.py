from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):   pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 700), 599
        self.speed = random.randint(1, 3)
        num = random.randint(0, 2)
        if num == 0:
            self.size = 21
            self.image = load_image('ball21x21.png')
        else:
            self.size = 41
            self.image = load_image('ball41x41.png')

    def update(self):
        if self.y >= 90 - self.size // 2:
            self.y -= 5 * self.speed

    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global team
    global world
    global balls

    running = True
    world = []

    # 원소 추가
    grass = Grass()
    world.append(grass)

    # 리스트 추가
    team = [Boy() for _ in range(10)]
    world += team

    balls = [Ball() for _ in range(20)]
    world += balls

def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world() # game logic
    render_world()  # draw world
    delay(0.05)

# finalization code

close_canvas()
