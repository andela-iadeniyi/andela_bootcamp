import turtle, math, polygon

def myTurtle():
    num_side = raw_input("Enter the number of sides: " )
    num_shap = raw_input("Enter the number of shapes: " )
    num_sides = int(num_side)
    num_shape = int(num_shap)
    #window = turtle.Screen()
   # window.bgcolor("red")
    #polygon = turtle.Turtle()
    side_length = polygon(100, num_sides)
    ''' 
    radius = 100
    angle = 360.0 // num_sides 
    delta = 100  #this value you must count
    colors = ['blue','white','black','green']
    for i in range(num_shape):
        polygon.penup()
        polygon.goto(-200+delta*i, 100)
        polygon.pendown()
        polygon.pencolor(colors[i%4])
        polygon.circle(radius)
        for j in range(num_sides):
            polygon.forward(side_length)
            polygon.right(angle)
    window.exitonclick()
    '''
    print side_length.find_lenth()

if __name__ == '__main__':
    myTurtle()