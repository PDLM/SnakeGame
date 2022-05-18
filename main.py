from turtle import Screen, Turtle
from snake import Snake
from food import  Food
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Stupid Snake Thing')
screen.tracer(0)

sam = Snake()
food = Food()

screen.listen()
screen.onkey(sam.up, "Up")
screen.onkey(sam.down, "Down")
screen.onkey(sam.left, "Left")
screen.onkey(sam.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    sam.move()
screen.exitonclick()
