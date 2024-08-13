from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.addScore()
        scoreboard.writeScore()

    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        gameIsOn = False
        scoreboard.gameOver()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        # elif snake.head.distance(segment) < 10:
        #     gameIsOn = False
        #     scoreboard.gameOver()

        if snake.head.distance(segment) < 10:
            gameIsOn = False
            scoreboard.gameOver()

screen.exitonclick()
