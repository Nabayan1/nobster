from turtle import Screen
from Snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:

    screen.update()  # For smoother animation
    time.sleep(0.1)
    snake.move()
    score.score_board()

    # detect collision with food
    if snake.head.distance(food) < 15:
        snake.elongate()
        print("nom nom nom")
        food.refresh()
        score.score_update()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 180 or snake.head.ycor() < -180:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            score.reset()
            snake.reset()


screen.exitonclick()

