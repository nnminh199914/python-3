colors = ['red', 'blue', 'brown', 'yellow', 'grey']
a=3
from turtle import *
for i in range(5):
    color(colors[i])
    for i in range(a):
        forward(50)
        left(360/a)
    a=a+1
        
