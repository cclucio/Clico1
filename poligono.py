import turtle
import time

tortuga=turtle.Turtle()
x=int(input('¿De cuantos lados desea dibujar el poligono?: '))

tortuga=turtle.Turtle()
for i in range(0,x):
    tortuga.forward(100)
    tortuga.left(360/x)
turtle.done()