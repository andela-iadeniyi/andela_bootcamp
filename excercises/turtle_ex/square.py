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
    radius = 50
    angle = 360.0 // num_sides
    window = turtle.Screen()
    window.bgcolor("red")
    polygon = turtle.Turtle()
    side_length = find_lenth(radius, num_sides)
    delta = side_length * 2
    #polygon.penup()
    for i in range(num_shape):
        #polygon.penup()
        polygon.penup()
        polygon.goto(-200+delta*i, 100)
        polygon.circle(radius)
        polygon.pendown() 
        for j in range(num_sides):
            polygon.forward(side_length)
            polygon.right(-angle)
        polygon.pencolor("blue")
        #polygon.forward(radius)
    window.exitonclick()

if __name__ == '__main__':
    print myTurtle()