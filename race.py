from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make the bet", prompt="Which turtle will win the race? Enter the color ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "purple", "blue"]
y_position = [-60, -30, 0, 30, 60, 90]
all_turtle=[]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-240, y=y_position[turtle_index])
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_turtle = turtle.pencolor()
            if user_bet == wining_turtle:
                print(f"You've Won!!!. The winning turtle is {wining_turtle}.")
            else:
                print(f"You've Lost!!!. The winning turtle is {wining_turtle}.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()