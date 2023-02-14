from turtle import Turtle, Screen

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self) -> None:
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for body in range(5):
            snake = Turtle('square')
            snake.pu()
            snake.color('white')
            snake.width = 20
            snake.goto((body * -20, 0))
            self.snakes.append(snake)

    def move(self):
        self.update_position()
        self.head.forward(20)
    
    def update_position(self):
        for snake in range(len(self.snakes) - 1, 0, -1):
            self.snakes[snake].goto(self.snakes[snake - 1].xcor(), self.snakes[snake - 1].ycor())

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)










