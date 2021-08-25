import turtle as t
import random


screen = t.Screen()
is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won. The {winning_turtle} turtle is the winner")
            else:
                print(f"You've lost. The {winning_turtle} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# tim = t.Turtle()
#
#
# def move_forward():
#     tim.forward(10)
#
#
# def move_backward():
#     tim.backward(10)
#
#
# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
#
# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
#
# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(move_forward, 'w')
# screen.onkey(move_backward, 's')
# screen.onkey(turn_left, 'a')
# screen.onkey(turn_right, 'd')
# screen.onkey(clear_screen, 'c')


screen.exitonclick()