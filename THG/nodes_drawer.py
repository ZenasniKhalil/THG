import turtle
from .style_config import * 

def draw_nodes(number_of_nodes, headers):
    # Now we will draw the graph
    # We want a big screen so we set the screen size as big as possible
    turtle.penup()  # We pick up the pen
    node_labels = headers
    couple = turtle.screensize()
    multiplier = 3 / 2
    screen_length = int(couple[0] * multiplier)
    screen_width = couple[1] * multiplier
    EAST, NORTH, WEST, SOUTH, DEGREES_CIRCLE, RADIUS = get_config_data()

    # screen_length, screen_width = turtle.screensize()
    turtle.screensize(screen_length, screen_width)  # We set the screen size
    # now we save the x and y coordinate of where we are
    x_origin = turtle.xcor()
    y_origin = turtle.ycor()

    couples_array = []  # This array will store the different coordinates of where we have our nodes

    angle_division = int(DEGREES_CIRCLE // number_of_nodes)
    angle_to_turn = angle_division
    direction = NORTH
    # Let's draw the first label
    small_step = 55
    turtle.setheading(NORTH)
    turtle.penup()
    turtle.forward(RADIUS)
    # save this coordinate
    couples_array.append([turtle.xcor(), turtle.ycor()])
   
    # move forward a bit more

    turtle.dot(40)

    turtle.forward(small_step)
    style = get_style_for_writing()
    turtle.pendown()
    # Now we write the node labels
    turtle.write(str(node_labels[0]), font=style, align='center')
    turtle.penup()  # pull the penup
    turtle.goto(x_origin, y_origin)  # go to origin
    turtle.setheading(NORTH)  # Face north
    small_step = 65
    # Now we draw the remaining labels
    for i in range(1, number_of_nodes):
        turtle.right(angle_to_turn)
        turtle.penup()
        turtle.forward(RADIUS)
        # save this coordinate
        couples_array.append([turtle.xcor(), turtle.ycor()])
        # here the palce of the dot node
        turtle.dot(40)
        n = number_of_nodes
        if float(i) >= 0.3 * n and float(i) <= 0.55 * n:
            small_step * 1.5
        # move forward a bit more
        turtle.forward(small_step+20)
        style = get_style_for_writing()
        turtle.pendown()
        # Now we write the node labels
        turtle.write(str(node_labels[i]), font=style, align='center')
        turtle.penup()  # pull the penup
        turtle.goto(x_origin, y_origin)  # go to origin
        turtle.setheading(NORTH)
        angle_to_turn += angle_division
    return couples_array