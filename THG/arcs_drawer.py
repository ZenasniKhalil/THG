import turtle
from .style_config import *


def draw_arcs(x_start, y_start, x_end, y_end,pcolor):
    couple = turtle.screensize()
    multiplier = 3 / 2
    screen_length = int(couple[0] * multiplier)
    screen_width = couple[1] * multiplier
    EAST, NORTH, WEST, SOUTH, DEGREES_CIRCLE, RADIUS = get_config_data()
    turtle.penup()  # We pull the pen up
    turtle.pensize(3)

    
    turtle.pencolor(pcolor)
    
    turtle.hideturtle()
    turtle.goto(x_start, y_start)
    turtle.showturtle()
    turtle.pendown()
    turtle.goto(x_end, y_end)
    heading = turtle.heading()
    #turtle.shape('circle')
    turtle.shapesize(2)
    turtle.setheading(heading)
    #turtle.stamp()
    turtle.penup()



def draw_arc_from_origin_to_dest(current_node,next_node,couples_array,pcolor):
    i = current_node
    j = next_node
    x_start = couples_array[i][0]
    y_start = couples_array[i][1]
    x_end = couples_array[j][0]
    y_end = couples_array[j][1]
    draw_arcs(x_start, y_start, x_end, y_end,pcolor)