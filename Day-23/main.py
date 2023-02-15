import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
cars = CarManager()
score = Scoreboard()

screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    score.update_score()
    cars.move(5 * score.level)
    if player.ycor() >= 280:
        player.reset_position()
        score.level += 1
    for car in cars.cars:
        if player.distance(car) < 20:
            game_is_on = False
    time.sleep(0.1)
    screen.update()

score.game_over()
screen.exitonclick()
