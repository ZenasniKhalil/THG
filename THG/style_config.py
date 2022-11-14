import turtle

def get_style_for_writing():
    style = ('Times Rew Romans', 15, 'bold')
    return style

def get_config_data():
    couple = turtle.screensize()
    multiplier = 3 / 2
    screen_length = int(couple[0] * multiplier)
    screen_width = couple[1] * multiplier
    EAST = 0
    NORTH = 90
    WEST = 180
    SOUTH = 270
    DEGREES_CIRCLE = 360
    RADIUS = (min(screen_length, screen_width) // 1.10)
    return EAST, NORTH, WEST, SOUTH, DEGREES_CIRCLE, RADIUS