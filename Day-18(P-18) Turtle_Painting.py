# Importing Modules
import turtle as t
import random

# Turtle characteristics
tim = t.Turtle()
t.colormode(255) # rgb to real color
tim.speed("fastest") # For speed 
tim.penup() # No Lines to draw while moving
tim.hideturtle() # Hide the turtle

# Random Colors
def randomcolors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color
colors = []
# Randomly taking 30 colors
for _ in range(30):
    x = randomcolors()
    colors.append(x)

# Starting Position
def start_posi():
    tim.penup()
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)

# Printing on every next line
def next_line():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(360)

num_of_dots = 100
# Print the dots as per number given
def print_dots():
    start_posi()
    for dot_count in range(1,num_of_dots+1):
        tim.dot(20,random.choice(colors))
        tim.forward(50)
        if dot_count % 10 == 0:
            next_line()

# START
print_dots()

# Screen Settings
screen = t.Screen()
screen.exitonclick()