import turtle
import time
t = turtle.Turtle()
def square(side,angle):
    t.fd(side)
    t.rt(angle)
    t.fd(side)
    t.rt(angle)
    t.fd(side)
    t.rt(angle)
    t.fd(side)
square(100,90)
turtle.done()