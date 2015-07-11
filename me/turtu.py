import turtle

def myTurtle():
	num_side = raw_input("Enter the number of sides: " )
	num_shap = raw_input("Enter the number of shapes: " )
	num_sides = int(num_side)
	num_shape = int(num_shap)
	window = turtle.Screen()
	window.bgcolor("red")

	polygon = turtle.Turtle()
	polygon.penup()
	polygon.goto(-200, 200)
	polygon.pendown()
	side_length = 60
	increase_by = 1
	angle = 360.0 // num_sides 
	n = 0

	for j in range(0, num_shape):
		polygon.forward(side_length)
		for i in range(num_sides):
			polygon.pencolor("black")
			polygon.forward(side_length)
			polygon.right(angle)
		n += side_length
    
 	window.exitonclick()

myTurtle()