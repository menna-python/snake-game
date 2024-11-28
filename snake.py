from turtle import Turtle
class Snake:
    def __init__(self):
        self.positions=[(-40,0),(-20,0),(0,0)]
        self.turtles=[]
        self.create_snake()

    def create_snake(self):
        for i in range (len(self.positions)):
            t=Turtle("square")
            t.color("white")
            t.penup()
            t.goto(self.positions[i])
            self.turtles.append(t)
        self.head=self.turtles[-1]

    def move(self):
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.head.forward(15)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)

    def extend(self):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.turtles[0].pos())
        self.turtles.insert(0,new_segment)
