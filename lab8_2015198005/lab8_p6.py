def drawSquare(myturtle, x, y, a):
    """
    function to draw a square
    :param myturtle: turtle drawing object
    :param x: x coordinate of turtle
    :param y: y coordinate of turtle
    :param a: length of each side
    """
    myturtle.penup()
    myturtle.setposition(x, y)  #move turtle to start location
    myturtle.pendown()  #start drawing
    for move in range(0, 4):    #draw four sides
        myturtle.forward(a)
        myturtle.left(90)

