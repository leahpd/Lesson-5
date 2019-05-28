from turtle import *

stardust = Turtle()

stardust.color("blue")
stardust.pensize(12)
stardust.speed(9)
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

# for x in range(18):
# 	square()
# 	stardust.left(20)


def triangle():
	stardust.forward(200)
	stardust.left(120)
	stardust.forward(200)
	stardust.left(120)
	stardust.forward(200)
	stardust.left(120)


# triangle()


for x in range(12):
	triangle()
	stardust.left(30)
mainloop()