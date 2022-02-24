from turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.tartarughe = []
        self.create_snake()
        self.head = self.tartarughe[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position ):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.tartarughe.append(turtle)

    def extend(self):
        self.add_segment(self.tartarughe[-1].position())

    def move(self):
        for seg_num in range(len(self.tartarughe) - 1, 0, -1):
            new_x = self.tartarughe[seg_num - 1].xcor()
            new_y = self.tartarughe[seg_num - 1].ycor()
            self.tartarughe[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
