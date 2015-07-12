import turtle

def myTurtle():
    num_side = raw_input("Enter the number of sides: " )
    num_shap = raw_input("Enter the number of shapes: " )
    num_sides = int(num_side)
    num_shape = int(num_shap)
    window = turtle.Screen()
    window.bgcolor("red")
    polygon = turtle.Turtle()
    side_length = 60
    angle = 360.0 // num_sides 
    delta = side_length*2  #this value you must count
    colors = ['blue','white','black','green']
    for i in range(0, 4):
    	
	    for i in range(num_shape):
	        polygon.penup()
	        polygon.goto(-200+delta*i, 200)
	        polygon.pendown()
	        polygon.pencolor(colors[i%4])
	        n = 0
	        for j in range(num_sides):
	            polygon.forward(side_length)
	            polygon.right(angle)
    window.exitonclick()

if __name__ == '__main__':
    myTurtle()