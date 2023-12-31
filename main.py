from turtle import Screen
from snake import Snake
import time
from food import Food
from score import ScoreBoard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=ScoreBoard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')


# #Snake Move Foward
game_is_on = True
while game_is_on:
    screen.update() 
    time.sleep(0.1)
    snake.move()
    #Detecting  with food:
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall:
    if abs(snake.head.xcor())>280 or  abs(snake.head.ycor() )> 280:
        # game_is_on = False 
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) <10:
            game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()


screen.exitonclick()