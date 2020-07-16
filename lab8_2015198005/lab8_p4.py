import turtle

turtle.setup(600, 600)  #set window size
window = turtle.Screen()    #get reference to turtle window

the_turtle = turtle.getturtle()
the_turtle.hideturtle() #hide turtle in window
the_turtle.penup()
the_turtle.setposition(-300, 300)
the_turtle.pendown()
the_turtle.setposition(300, -300)
the_turtle.penup()
the_turtle.setposition(300, 300)
the_turtle.pendown()
the_turtle.setposition(-300, -300)

window.exitonclick()    #exit window