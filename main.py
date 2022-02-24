import turtle
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboording import Score
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect the collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()


    # detect collision with a wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        score.game_over()

    #detect collisio with tail
    for segment in snake.tartarughe[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()





































screen.exitonclick()

