import turtle as t
import random
tim = t.Turtle()

t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(50)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     tim.color(random_color())
#     draw_shape(shape_side_n)

# tim.pensize(15)
# tim.speed('fastest')
# directions = [0, 90, 180, 270]
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

tim.speed('fastest')
def draw_spirograf(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograf(3)


screen = t.Screen()
screen.exitonclick()