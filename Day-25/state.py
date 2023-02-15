from turtle import Turtle
import pandas as pd


class State(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.data = pd.read_csv('Day-25/50_states.csv')

    def show_state(self, state):
        if len(self.data[self.data['state'] == state]) > 0:
            state_data = self.data.loc[self.data.state == state]
            self.goto(int(state_data.x.values[0]), int(state_data.y.values[0]))
            self.write(f"{state_data.state.values[0]}")