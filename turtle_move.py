#Drill 01
import turtle

def up_move():
    turtle.setheading(90)   # 북쪽으로
    turtle.forward(50)

def down_move():
    turtle.setheading(270)   # 남쪽으로
    turtle.forward(50)
    
def left_move():
    turtle.setheading(180)   # 서쪽으로
    turtle.forward(50)

def right_move():
    turtle.setheading(0)   # 동쪽으로
    turtle.forward(50)

def restart():
    turtle.reset()

turtle.shape('turtle')

