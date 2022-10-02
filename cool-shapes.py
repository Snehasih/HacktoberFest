from turtle import *
bgcolor('black')
speed(0)
hideturtle()
for  i in range(120):
    color('red')
    circle(i)
    color('orange')
    circle(i*0.8)
    color('white')
    circle(i*1.6)
    right(3)
    backward(5)

done()