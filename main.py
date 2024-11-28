from turtle import Screen
import turtle
from tkinter import *
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

window=Screen()
window.title("snake game")
window.setup(800,800)
window.bgcolor("black")

def on_close():
    global game_on
    game_on = False  # Stop the game loop
    try:
        window.bye()  # Close the Turtle graphics window
    except turtle.Terminator:
        pass 
window.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", on_close)

window.tracer(0)

sam=Snake()
f=Food()
score=Scoreboard()

game_on=True
try:
    while game_on:
        sam.move()
        time.sleep(0.1)
        window.listen()
        window.onkey(sam.up,"Up")
        window.onkey(sam.down,"Down")
        window.onkey(sam.right,"Right")
        window.onkey(sam.left,"Left")
        
        if sam.head.distance(f)<15:
            f.appear()
            sam.extend()
            score.increase_score()

        if sam.head.xcor()>375 or sam.head.xcor()<-375 or sam.head.ycor()>375 or sam.head.ycor()<-375:
            score.game_over()
            window.update()
            time.sleep(3)  
            on_close()
            
        for segment in sam.turtles[:-1]:
            if sam.head.distance(segment)<10:
                score.game_over()
                window.update()
                time.sleep(3)  
                on_close()
        
        window.update()

except turtle.Terminator:
    pass
    
