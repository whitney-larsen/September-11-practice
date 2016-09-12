import turtle
window = turtle.Screen()
window.bgcolor("red")
turtle.pencolor("blue")

def draw_star():
    for x in range(9):
    	turtle.forward(100)
        turtle.right(160)

def draw_circles():
	for x in range(20):
		turtle.circle(50)
		turtle.right(20)

def main():
	turtle.pendown()
	draw_circles()
	window.exitonclick()


if __name__ == '__main__':
    main()
