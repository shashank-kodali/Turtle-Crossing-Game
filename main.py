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
scoreboard = Scoreboard()
cars = CarManager()

screen.onkey(player.moveForward,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.createcCar()
    cars.moveCars()

    if (player.ycor() >=280):
        player.start()
        scoreboard.updateScoreBoard()
        cars.increaseSpeed()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.gameOver()
            game_is_on = False


screen.exitonclick()

    

