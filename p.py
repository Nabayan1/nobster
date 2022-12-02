from turtle import Turtle


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []

    def show(self):
        for x in range(0, 2):
            self.segments[x].goto(100, 100)

    def generate(self):
        for x in range(0, 2):
            new_seg = Turtle(shape="square")
            new_seg.penup()
            new_seg.turtlesize(2)
            self.segments.append(new_seg)




