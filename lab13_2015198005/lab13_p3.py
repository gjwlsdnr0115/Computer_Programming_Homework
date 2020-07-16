
# Import our own constants:
from globals import FOODMAX, STEPMAX, WIDTH, HEIGHT, X_MAX, Y_MAX, MS_TO_QUIT
from globals import FOOD as food, GHOSTS as ghosts

# Import our own doboggi_man class:
from characters import doboggi_man 

import turtle


class auto_doboggi_man(doboggi_man):

    """
    Class auto_doboggi_man, the autonomous doboggi-collector.

    The auto_doboggi_man class is a subclass of the doboggi_man class. It
    inherits all data attributes and methods from the doboggi_man class. It
    overrides the move() method of the doboggi_man class to automatically
    navigate doboggi_man across the screen.

    Attributes:
    ... Please describe your attributes here
    """

    def __init__(self, x=0, y=0):
        doboggi_man.__init__(self, x, y)
        self.score = 0
        self.bottom = True

    def move(self):
        # Don't move beyond screen border:
        if self.dir == 'east' and self.ttl.xcor() > X_MAX:
            return
        if self.dir == 'west' and self.ttl.xcor() < -X_MAX:
            return
        if self.dir == 'north' and self.ttl.ycor() > Y_MAX:
            return
        if self.dir == 'south' and self.ttl.ycor() < -Y_MAX:
            return


        if self.score == 0:
            x, y = food[1].getPosition()

            if x - self.ttl.xcor() >= 10:
                self.turnEast()
                self.ttl.forward(10)
            elif 10 > x - self.ttl.xcor() > 0:
                self.turnEast()
                self.ttl.forward(x-self.ttl.xcor())
            elif -10 < x - self.ttl.xcor() < 0:
                self.turnWest()
                self.ttl.forward(self.ttl.xcor() - x)
            elif x - self.ttl.xcor() <= -10:
                self.turnWest()
                self.ttl.forward(10)
            else:
                if y - self.ttl.ycor() >= 10:
                    self.turnNorth()
                    self.ttl.forward(10)
                elif 10 > y - self.ttl.ycor() > 0:
                    self.turnNorth()
                    self.ttl.forward(y - self.ttl.ycor())
                    self.score = 1
                elif -10 < y - self.ttl.ycor() < 0:
                    self.turnSouth()
                    self.ttl.forward(self.ttl.ycor() - y)
                    self.score = 1
                elif y - self.ttl.ycor() <= -10:
                    self.turnSouth()
                    self.ttl.forward(10)

        if self.score == 1 and self.bottom:
            self.turnNorth()
            safe = True
            for ghost in ghosts:
                gx, gy = ghost.ttl.getPosition()
                next_g_pos = (gx + 10, gy)
                x, y = self.ttl.getPosition()
                next_pos = (x, y + 10)
                if (abs(next_pos[0] - next_g_pos[0]) < 25) and (abs(next_pos[1] - next_g_pos[1]) < 25):
                    safe = False
            if safe:
                self.ttl.forward(10)
            else:
                self.ttl.forward(0)

            if self.ttl.ycor() > 120:
                self.bottom = False

        if self.score == 1 and not self.bottom:
            x, y = food[0].getPosition()
            if x - self.ttl.xcor() >= 10:
                self.turnEast()
                self.ttl.forward(10)
            elif 10 > x - self.ttl.xcor() > 0:
                self.turnEast()
                self.ttl.forward(x - self.ttl.xcor())
            elif -10 < x - self.ttl.xcor() < 0:
                self.turnWest()
                self.ttl.forward(self.ttl.xcor() - x)
            elif x - self.ttl.xcor() <= -10:
                self.turnWest()
                self.ttl.forward(10)
            else:
                if y - self.ttl.ycor() >= 10:
                    self.turnNorth()
                    self.ttl.forward(10)
                elif 10 > y - self.ttl.ycor() > 0:
                    self.turnNorth()
                    self.ttl.forward(y - self.ttl.ycor())
                    self.score = 2
                elif -10 < y - self.ttl.ycor() < 0:
                    self.turnSouth()
                    self.ttl.forward(self.ttl.ycor() - y)
                    self.score = 2
                elif y - self.ttl.ycor() <= -10:
                    self.turnSouth()
                    self.ttl.forward(10)

        if self.score == 2 and not self.bottom:
            x, y = food[0].getPosition()
            if x - self.ttl.xcor() >= 10:
                self.turnEast()
                self.ttl.forward(10)
            elif 10 > x - self.ttl.xcor() > 0:
                self.turnEast()
                self.ttl.forward(x - self.ttl.xcor())
            elif -10 < x - self.ttl.xcor() < 0:
                self.turnWest()
                self.ttl.forward(self.ttl.xcor() - x)
            elif x - self.ttl.xcor() <= -10:
                self.turnWest()
                self.ttl.forward(10)
            else:
                if y - self.ttl.ycor() >= 10:
                    self.turnNorth()
                    self.ttl.forward(10)
                elif 10 > y - self.ttl.ycor() > 0:
                    self.turnNorth()
                    self.ttl.forward(y - self.ttl.ycor())
                elif -10 < y - self.ttl.ycor() < 0:
                    self.turnSouth()
                    self.ttl.forward(self.ttl.ycor() - y)
                elif y - self.ttl.ycor() <= -10:
                    self.turnSouth()
                    self.ttl.forward(10)

            




        # Change this code to make your doboggi_man navigate the screen
        # and collect all doboggi.
        #self.ttl.forward(0)
        #
        # Uncomment to dump positions in the PyCharm console window:
        #
        #print(ghosts[0], ghosts[1])
        #print(food[0], food[1], food[2])
