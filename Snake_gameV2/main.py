# Read Method
# with open("data_memory.txt") as file:
    # contents = file.read()
    # print(contents)

# Write Method with write mode:
# with open("data_memory.txt",mode="w") as file:
    #file.write("New text")

# Write Method with adding written mode:
# with open("data_memory.txt",mode="a") as file:
    #file.write("\nadded something")

# Write in a created file:
# with open("new_file.txt",mode="a") as file:
    # file.write("\n write in a new file")

#--------------------------------------------------

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    #Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
           scoreboard.reset()
           snake.reset()





screen.exitonclick()
