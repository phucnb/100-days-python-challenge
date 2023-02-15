from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.hideturtle()
        self.color('white')
        self.goto(-250, 260)
        self.highest_score = self.read_highest_score()
        self.display_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        if self.score > self.highest_score:
            self.update_highest_core()
        self.display_score()

    def display_score(self):
        self.highest_score = self.read_highest_score()
        self.goto(-250, 260)
        self.write(f"Score: {self.score}",align='center', font=('Arial', 20, 'normal'))
        self.goto(0, 260)
        self.write(f"Highest Score: {self.highest_score}",align='right', font=('Arial', 20, 'normal'))


    def game_over(self):
        self.clear()
        self.goto(-200, 0)
        self.write(f"GAME OVER", font=('Arial', 60, 'normal'))
        self.goto(-40, -60)
        self.write(f"Score: {self.score}", font=('Arial', 20, 'normal'))

    def read_highest_score(self):
        with open("Day-24/score.txt") as file:
            # self.highest_score = int(file.read())
            return int(file.read())

    def update_highest_core(self):
        with open("Day-24/score.txt", 'w') as file:
            file.write(str(self.score))