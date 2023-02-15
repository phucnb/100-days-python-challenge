from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.hideturtle()
        self.color('white')
        self.goto(-40, 280)
        self.write(f"Score: {self.score}", font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.color('white')
        self.write(f"Score: {self.score}", font=('Arial', 20, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(-200, 0)
        self.write(f"GAME OVER", font=('Arial', 60, 'normal'))
        self.goto(-40, -60)
        self.write(f"Score: {self.score}", font=('Arial', 20, 'normal'))