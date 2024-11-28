from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,350)
        self.hideturtle()
        self.score=0
        self.show_score()

    def show_score(self):
        self.write(f"Score:{self.score}",align="center",font={"arial",20,"bold"})

    def increase_score(self):
        self.score+=1
        self.clear()
        self.show_score()

    def game_over(self):
        self.screen.bgcolor("navy")
        self.goto(0,0)
        self.write(f"Game over\nFinal score:{self.score}",align="center",font={"arial",20,"bold"})
        