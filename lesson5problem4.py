from turtle import *

stardust = Turtle()

stardust.color("blue")
stardust.pensize(12)
stardust.speed(9)
stardust.shape("turtle")

def hexagon(s):
	for x in range(6):
		stardust.forward(s)
		stardust.left(60) 

# hexagon(30)
# hexagon(50)
# hexagon(70)
# hexagon(90)
# hexagon(110)

for x in range(10,200,20):
	hexagon(x)

mainloop()