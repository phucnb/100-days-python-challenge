from turtle import Turtle, Screen
from random import randint

width = 1200
height = 600
final_x = width / 2 - 40
screen = Screen()
winner = Turtle()
winner.hideturtle()
screen.setup(width = width, height = height)
bet = screen.textinput(title="your bet", prompt = 'Which turtle will win:')
turtles = [Turtle('turtle') for _ in range(6)]
colors = ['red', 'blue', 'yellow', 'green', 'orange', 'purple']
for turtle in range(len(turtles)):
    turtles[turtle].pu()
    turtles[turtle].color(colors[turtle])
    turtles[turtle].goto(x = -width / 2 + 20, y = (-height / 2 + 40) + (turtle * height / 6))

line = Turtle()
line.hideturtle()
line.pu()
line.goto(x = final_x, y = (-height / 2 + 40) + (0 * height / 6))
line.pd()
line.goto(x = final_x, y = (-height / 2 + 40) + (6 * height / 6))

finish = False
while not finish:
    for turtle in turtles:
        turtle.speed(0)
        turtle.forward(randint(1, 20))
        if turtle.xcor() > final_x:
            winner = turtle
            finish = True
    
result = "Win" if winner.color()[0] == bet else "Lose"
text = Turtle()
text.hideturtle()

text.write(result, font=('Arial', 50, 'normal'))









screen.exitonclick()