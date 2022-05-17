from turtle import Screen, Turtle
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Stupid Snake Thing')
screen.tracer(0)


snake_body = []
i = 0
for square in range(0,3):

    square = Turtle()
    square.shape("square")
    square.penup()
    square.color("white")
    square.goto(0 - (20*i), 0)
    i += 1
    snake_body.append(square)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    for segment in range(len(snake_body)-1, 0, -1):
        new_x = snake_body[segment - 1].xcor()
        new_y = snake_body[segment - 1].ycor()
        snake_body[segment].goto(new_x, new_y)
    snake_body[0].forward(20)

screen.exitonclick()
