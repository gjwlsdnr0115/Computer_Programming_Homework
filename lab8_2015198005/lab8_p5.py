import turtle
import random
import time


def atLeftEdge(ball, screen_width):
    if ball.xcor() < -screen_width / 2:
        return True
    else:
        return False


def atRightEdge(ball, screen_width):
    if ball.xcor() > screen_width / 2:
        return True
    else:
        return False


def atTopEdge(ball, screen_height):
    if ball.ycor() > screen_height / 2:
        return True
    else:
        return False


def atBottomEdge(ball, screen_height):
    if ball.ycor() < -screen_height / 2:
        return True
    else:
        return False


def bounceBall(ball, new_direction):
    if new_direction == 'left' or new_direction == 'right':
        new_heading = 180 - ball.heading()
    elif new_direction == 'down' or new_direction == 'up':
        new_heading = 360 - ball.heading()
    return new_heading

def changeColor(ball):
    """
    function to change ball color
    :param ball: ball to mutate
    :return: no return value
    """
    same_color = True   #identical to previous color
    ball_color = ball.color()[1]    #get fill color
    while same_color:
        new_color = random.choice(colors) #pick random color
        if new_color != ball_color:     #if different from previous color
            ball.fillcolor(new_color)   #change color
            same_color = False


def createBalls(num_balls, colors):
    balls = []
    ball_colors = colors
    for k in range(0, num_balls):
        new_ball = turtle.Turtle()
        new_ball.shape('circle')
        color = random.choice(ball_colors)
        new_ball.fillcolor(color)
        ball_colors.remove(color)
        new_ball.speed(0)
        new_ball.pendown()
        new_ball.setheading(random.randint(1, 359))
        balls.append(new_ball)

    return balls


# ---- main
# program greeting
print('This program simulates bouncing balls in a turtle screen')
print('for a specified number of seconds.')

# init screen size
screen_width = 800
screen_height = 600
turtle.setup(screen_width, screen_height)

# create turtle window
window = turtle.Screen()
window.title('Bouncing Balls')

# prompt user for execution time and number of balls
num_seconds = int(input('Enter number of seconds to run: '))
num_balls = 3

#list of colors to fill ball
colors = ['red', 'blue', 'green', 'yellow', 'brown', 'gray', 'black', 'violet']

# create balls
balls = createBalls(num_balls, colors)

# set start time
start_time = time.time()

# begin simulation
terminate = False

while not terminate:
    for k in range(0, len(balls)):
        balls[k].forward(15)

        if atLeftEdge(balls[k], screen_width):
            balls[k].setheading(bounceBall(balls[k], 'right'))
            changeColor(balls[k])   #change color
        elif atRightEdge(balls[k], screen_width):
            balls[k].setheading(bounceBall(balls[k], 'left'))
            changeColor(balls[k])

        if atTopEdge(balls[k], screen_height):
            balls[k].setheading(bounceBall(balls[k], 'down'))
            changeColor(balls[k])
        elif atBottomEdge(balls[k], screen_height):
            balls[k].setheading(bounceBall(balls[k], 'up'))
            changeColor(balls[k])

        if time.time() - start_time > num_seconds:
            terminate = True

# exit on close window
turtle.exitonclick()
