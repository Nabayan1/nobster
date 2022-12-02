from turtle import Turtle
position = [(20, 0), (0, 0), (-20, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for n_turtle in range(0, 3):
            new_turtle = Turtle(shape="square")
            new_turtle.color("purple")
            new_turtle.penup()
            new_turtle.setposition(position[n_turtle])
            self.segments.append(new_turtle)

    def move(self):
        for segnum in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segnum - 1].xcor()
            new_y = self.segments[segnum - 1].ycor()
            self.segments[segnum].goto(new_x, new_y)
        self.head.forward(18)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def elongate(self):
        new_segment = Turtle(shape="square")
        new_segment.color("purple")
        new_segment.penup()
        if self.segments[-1].heading() == 0 or self.segments[-1].heading() == 180:
            new_segment.goto(self.segments[-1].xcor() - 20, self.segments[-1].ycor())
        elif self.segments[-1].heading() == 90 or self.segments[-1].heading() == 270:
            new_segment.goto(self.segments[-1].xcor(), self.segments[-1].ycor() - 20)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

