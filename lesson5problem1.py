from turtle import *

stardust = Turtle()

stardust.color("blue")
stardust.pensize(12)
stardust.speed(2)
stardust.shape("turtle")

# Define what it means to draw a square
def square():
	stardust.forward(100)
	stardust.left(90)
	stardust.forward(100)
	stardust.left(90)
	stardust.forward(100)
	stardust.left(90)
	stardust.forward(100)
	stardust.left(90)

# Use the square function to actually run the new procedure


def triangle():
	stardust.forward(45)
	stardust.left(120)
	stardust.forward(45)
	stardust.left(120)
	stardust.forward(45)
	stardust.left(120)

triangle()

mainloop()