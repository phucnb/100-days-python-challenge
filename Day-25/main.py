from turtle import Turtle, Screen
import pandas as pd
from state import State


data = pd.read_csv('Day-25/50_states.csv')

screen = Screen()
screen.setup(width=725, height=491)
screen.bgpic("Day-25/blank_states_img.gif")
screen.tracer(0)
state = State()
game_on = True



while game_on:
    input = screen.textinput("Guess a state", "Name of a US's State")
    state.show_state(input.title())
screen.update()
screen.exitonclick()