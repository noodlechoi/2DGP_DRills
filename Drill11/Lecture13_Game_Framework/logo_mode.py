from pico2d import load_image, clear_canvas, update_canvas, get_events, get_time
import game_framework
import title_mode


def init():
    global image
    global running
    global logo_start_time

    running = True
    image = load_image('tuk_credit.png')
    logo_start_time = get_time()

def finish():
    global image
    del image

def update():
    global logo_start_time
    if get_time() - logo_start_time >= 2.0:
        logo_start_time = get_time()
        game_framework.change_mode(title_mode)

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    pass