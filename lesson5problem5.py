from turtle import *

stardust = Turtle()

stardust.color("blue")
stardust.pensize(6)
stardust.speed(9)
stardust.shape("turtle")

def star():
	for x in range(5):
		stardust.forward(50)
		stardust.left(144) 

star()

mainloop()