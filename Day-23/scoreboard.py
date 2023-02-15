from turtle import Turtle
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.level = 1
        self.goto(-260, 260)
        
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(-30, 0)
        self.write("GAME OVER", font=FONT)
