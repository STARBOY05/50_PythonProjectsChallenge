# Modules
from turtle import Screen, Turtle
import turtle
import random
# Turtle Settings
colors = ["red","blue","green","purple","orange","yellow"]
y_posi = [-70, -40, -10, 20, 50, 80]
all_turtles = []
# Screen Settings
screen = turtle.Screen()
screen.setup(width=500, height=400)
# Creation of referee Turtle
ref = Turtle()
ref.shape("arrow")
ref.hideturtle()

def refereeT(line):
    x = 230
    ref.penup()
    if line == "start":       
        ref.goto(-x+10,-180)
    elif line == "finish":
        ref.goto(x,-180)
    for _ in range(1):
        ref.setheading(90)
        ref.pendown()
        ref.forward(350)

refereeT("start")
refereeT("finish")

# Creation of 6 turtles
for turtle_index in range(0,6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.speed("slow")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    # Turtle Position
    new_turtle.goto(x=-230,y=y_posi[turtle_index])
    all_turtles.append(new_turtle)

# Asking for bet
user_bet = screen.textinput(title="The TURTLE race", prompt="On which turtle you will bet on? Enter the color: ")
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 225:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f"You've Won! The {winning_turtle} turtle is the winner.")
            else:
                print(f"You've Lost! The {winning_turtle} turtle is the winner.")
        dist = random.randint(0,10)
        turtle.forward(dist)

# Screen Settings
screen.exitonclick()