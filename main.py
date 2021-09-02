from turtle import Screen
from snake import Snake
from food import Food
from score_board import Score

import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")

# Name of the window
screen.title("My Snake game")
# turn off the tracer
screen.tracer(0)

# ------ 1: Create a snake body ----------
my_snake = Snake()
my_snake.create_snake()

# ------- 4: inititalize food -------------
food = Food()
# ----- 5: Create the Scoreboard ----------
scoreboard = Score()


# ------ 3: add event listener to control the snake  binded with methods from snake object ------
screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")



# -------- 2: Move the snake's direction ---------

game_is_on = True

while game_is_on:
    # update the screen by scene in the way that different peaces follow the body itself
    screen.update()
    # add one second delay refresh every 0.1s
    time.sleep(0.1)
    # on move each segments have to follow each other (move forward)
    my_snake.move()


# ---------- 4: Detect collision with food -------------------
    # Using distance method from the turtle class:
    if my_snake.head.distance(food) < 15: # => this value is ruffly = to one pixel
        food.refresh()
        scoreboard.set_score()
    # Extend the snake once it reachs the food
        my_snake.extend()

# ---------- 6: Detect collision with wall --------------------
    if my_snake.head.xcor() > 290 or my_snake.head.xcor() < - 290 or my_snake.head.ycor() > 290 or my_snake.head.ycor() < - 290:
        game_is_on = scoreboard.game_over()

# ---------- 7: Detect collision with Tail ---------------------
    for segment in my_snake.segments[1:]:
        if segment == my_snake.head:
            pass
        elif my_snake.head.distance(segment) < 10:
            game_is_on = scoreboard.game_over()


screen.exitonclick()
