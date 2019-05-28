from turtle import *

stardust = Turtle()

stardust.color("blue")
stardust.pensize(12)
stardust.speed(9)
stardust.shape("turtle")

def hexagon():
	for x in range(6):
		stardust.forward(30)
		stardust.left(60) 
		
hexagon()
mainloop()