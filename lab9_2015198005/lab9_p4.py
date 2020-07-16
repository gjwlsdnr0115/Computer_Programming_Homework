import turtle

def drawFlower(myturtle, r):
    """Draws a flower composed of 24 circles
    on the screen. The radius of the
    circles is ``r''.
    The drawing color is ``red''.
    The turtle ``myturtle '' is already
    positioned in the center of the flower.
    """
    myturtle.pencolor('red')    #set pen color to red
    myturtle.hideturtle()       #hide turtle
    for i in range(24):         #draw 24 circles
        myturtle.circle(r)      #draw circle
        myturtle.left(15)       #tilt turtle left 15 degrees (360 / 24 = 15)
