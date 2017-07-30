colors = ['red', 'blue', 'brown', 'yellow', 'grey']
from turtle import *
for i in range(5):
    begin_fill()
    color(colors[i])
    penup()
    forward(50)
    pendown()
    for i in range(4):
        forward(50)
        left(90)
    end_fill()  
       
