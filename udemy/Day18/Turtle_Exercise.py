import turtle as t
import random

#1
#timmy = t.Turtle()

#for _ in range(4):
#    timmy.forward(100)
#    timmy.left(90)

#2
#tim = t.Turtle()

#for _ in range(15):
#    tim.forward(10)
#    tim.penup()
#    tim.forward(10)
#    tim.pendown()

#3
#tim = t.Turtle()
#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
#def draw_shape(num_sides):
#    angle = 360 / num_sides
#    for _ in range(num_sides):
#        tim.forward(100)
#        tim.right(angle)
#
#for shape_side_n in range(3, 10):
#    tim.color(random.choice(colours))
#    draw_shape(shape_side_n)

#4
#tim = t.Turtle()
#
#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#directions = [0, 90, 180, 270]
#tim.pensize(15)
#tim.speed("fastest")
#
#for _ in range(200):
#    tim.color(random.choice(colours))
#    tim.forward(30)
#    tim.setheading(random.choice(directions))

#5
#tim = t.Turtle()
#t.colormode(255)
#def random_color():
#    r = random.randint(0, 255)
#    g = random.randint(0, 255)
#    b = random.randint(0, 255)
#    color = (r, g, b)
#    return color
#
#def draw_spirograph(size_of_gap):
#    for _ in range(int(360 / size_of_gap)):
#        tim.color(random_color())
#        tim.circle(100)
#        tim.setheading(tim.heading() + size_of_gap)
#
#draw_spirograph(5)