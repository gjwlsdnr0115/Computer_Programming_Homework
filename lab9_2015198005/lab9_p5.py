#
# Please save this program to the hard-drive of your computer and set
# it up as a PyCharm project.
#

import turtle

def square(t, length):
  for s in range(4):
    t.forward(length)
    t.left(90)

def writeText():
  '''
  Writes the coordinates of the turtle at position (0, 0)
  '''
  t2.clear()  #clear turtle t2
  xpos = str(int(t.position()[0]))   #x position of turtle as integer, then convert to string
  ypos = str(int(t.position()[1]))   #y position of turtle

  #write coordinates
  t2.write('('+xpos+', '+ypos+')', font=('Times New Roman', 8, 'bold'))

def closeDown():
  turtle.bye()

def drawShape(x, y):
  t.penup()
  t.setpos(x, y)
  t.pendown()
  t.begin_fill()
  if x <= 100: #Left third:
    t.color("green")
    square(t, 10)
  elif 100 < x <= 200: #Middle third:
    t.color("red")
    t.circle(10)
  else:
    t.color("blue")
    square(t, 10)
  t.end_fill()

#
# main:
#

# Set window to be 300 x 200 with the point (0, 0) as the lower-left
# corner and (300, 200) as the upper right corner:
turtle.setup(300, 200)
turtle.screensize(300, 200)
turtle.setworldcoordinates(0, 0, 300, 200)

# Initialize global turtle t variable which will be used inside
# of the handler functions:
t = turtle.getturtle()
t.speed(0) # Set fastest screen update speed for this turtle.

# Draw two vertical lines to divide the window into thirds:
t.penup()
t.setpos(100, 0) #First line
t.pendown()
t.setpos(100, 200)
t.penup()
t.setpos(200, 0) #Second line
t.pendown()
t.setpos(200, 200)

#create second turtle to write coordinates
t2 = turtle.Turtle()
t2.speed(0)   #set fastest speed
t2.penup()
t2.setpos(0, 0)   #set position
t2.pendown()

# Register callback for key-press events:
turtle.onkey(writeText, 'Up')
turtle.onkey(closeDown, 'q')
# Register callback for mouse on-click events:
turtle.onscreenclick(drawShape)
# Enter event loop:
turtle.listen()
turtle.mainloop()
