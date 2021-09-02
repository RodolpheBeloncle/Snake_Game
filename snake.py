
from turtle import Turtle
# refactoring snake part with OOP Class

# my way to build class
#class Snake():

    #def __init__(self):
    # create a tupple_list for coordonates:
        #self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]

    # create segments_list (peaces)
        #self.segments = []

    #def snake_bulder(self):
        # ------ 1: Create a snake body ----------

        # Build The Snake
        #for size_snake in range(0, 3):
            #new_peace_snake = turtle.Turtle(shape="square")
            #new_peace_snake.penup()
            #new_peace_snake.color("white")
            #new_peace_snake.goto(self.starting_positions[size_snake])
            #self.segments.append(new_peace_snake)

    #def move(self):
        #for seg_number in range(len(self.segments) - 1, 0, -1):  # follow parameter (start,stop,step)
            #new_x = self.segments[seg_number - 1].xcor()
            #new_y = self.segments[seg_number - 1].ycor()
            # each segment[index] have to go the position from the second to the last segment
            #self.segments[seg_number].goto(new_x, new_y)
        #self.segments[0].forward(20)


# Angela 's way to build class
# create a tupple_list for coordonates:
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] # => tupple's list of different segement's position
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]




    def create_snake(self):
        for size_snake in STARTING_POSITIONS:
            self.add_segment(size_snake)


    def add_segment(self, size_snake):
        new_peace_snake = Turtle(shape="square")
        new_peace_snake.penup()
        new_peace_snake.color("white")
        new_peace_snake.goto(size_snake)
        self.segments.append(new_peace_snake)

    def move(self):
        for seg_number in range(len(self.segments) - 1, 0, -1):  # follow parameter (start,stop,step)
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
        #each segment[index] on move have to go the position from the second to the last segment
            self.segments[seg_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # methods to move the head of the snake
    def up(self):
        # !! if the direction is heading down/up/left/right rules not allowed to reverse the direction !!
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def extend(self):
        self.add_segment(self.segments[-1].position())