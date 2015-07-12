import turtle, math

def find_lenth(radius, sides):
    angle = float(360 / sides)
    otherangle = float((180 - angle) / 2)
    radangle = float(angle * (math.pi / 180))
    radangle2 = float(otherangle * (math.pi/180))
    angles = math.sin(radangle) / math.sin(radangle2)
    lenth = radius * angles
    return lenth    

def myTurtle():
    num_side = raw_input("Enter the number of sides: " )
    num_shap = raw_input("Enter the number of shapes: " )
    num_sides = int(num_side)
    num_shape = int(num_shap)
    window = turtle.Screen()
    window.bgcolor("red")
    polygon = turtle.Turtle()
    radius = 60
    side_length = find_lenth(radius, num_sides)
    angle = 360.0 // num_sides 
    delta = side_length  #this value you must count
    colors = ['blue','white','black','green']
    for i in range(num_shape):
        polygon.penup()
        polygon.goto(-400+delta*i, 200)
        polygon.pendown()
        polygon.pencolor(colors[i%4])
        n = 0
        for j in range(num_sides):
            polygon.forward(side_length)
            polygon.right(angle)
    window.exitonclick()

if __name__ == '__main__':
    myTurtle()