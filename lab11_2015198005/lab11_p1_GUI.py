import time
import turtle

SIZE=20 # size of the 2D cellular automaton
work = []
tmp  = []

def printSep():
    '''Print a separator'''
    for ctr in range(0, SIZE+2):
        print('-', end='')
    print('')


def printWorld(world):
    '''Print one generation.
       Must use printSep() above to print the separators.
    '''

    printSep()
    for i in range(SIZE):   #print each row
        print('|', end='')
        for j in range(SIZE):
            if world[i][j] == 0:
                print(' ', end='')
            else:
                print('x', end='')
        print('| row', i)   #add row number
    printSep()


def printTurtle(s, t):
    '''function that writes the generation'''
    t.write(s, font=('Times New Roman', 12, 'bold'))

def add_to_string(world):
    '''
    returns the content of the variable world in string format
    :param world: input world
    :return: string
    '''
    s = ''
    s += '-'*(SIZE+2)
    s+='\n'
    for i in range(SIZE):
        s+='|'
        for j in range(SIZE):
            if world[i][j] == 0:
                s+=' '
            else:
                s+='x'
        s+='| row '
        s+= str(i)
        s+='\n'
    s += '-' * (SIZE + 2)
    s += '\n'
    return s


def compute(world, i, j):
    '''
    Computes and returns the next generation value of the given cell
    :param world: 2d world
    :param i: row of cell
    :param j: column of cell
    :return: next value
    '''
    #init num of neighbors
    neighbors = 0
    #start and end of neighbor index
    start_i = i-1
    start_j = j-1
    end_i = i+1
    end_j = j+1

    #if start/end index is out of 2d grid
    if start_i < 0:
        start_i = 0
    if start_j < 0:
        start_j = 0
    if end_i > SIZE-1:
        end_i = SIZE-1
    if end_j > SIZE-1:
        end_j = SIZE-1

    #length of neighbors
    i_len = end_i - start_i + 1
    j_len = end_j - start_j + 1

    #count neighbors
    for k in range(i_len):
        for l in range(j_len):
            if world[start_i + k][start_j + l] == 1:
                neighbors += 1
    if world[i][j] == 1:
        neighbors -= 1

    #return next generation value
    if world[i][j] == 1 and neighbors < 2:
        return 0
    if world[i][j] == 1 and (neighbors == 2 or neighbors == 3):
        return 1
    if world[i][j] == 1 and neighbors > 3:
        return 0
    if world[i][j] == 0 and neighbors == 3:
        return 1
    return world[i][j]
#
# Main program
#

#user input
try:
    inp = int(input('Grid sidelength (default 20): '))
except ValueError:
    #if error, input = 20
    inp = 20

if(inp < 20):
    inp = 20

SIZE = inp


ValidInput = False
while not ValidInput:
    #loop until not faulty input
    try:
        generation = int(input('Max generation: '))
        if generation > 0:
            ValidInput = True
    except ValueError:
        ValidInput = False


# Initialize work and tmp:

for i in range(SIZE):
    tmp = [0]*SIZE
    work.append(tmp)


work[0][1] = 1
work[1][1] = 1
work[2][1] = 1
work[10][11] = 1
work[10][12] = 1
work[10][13] = 1
work[11][11] = 1
work[12][11] = 1
work[12][12] = 1
work[12][13] = 1

#initialize turtle
t = turtle.getturtle()
t.hideturtle()
t.penup()
t.setpos(-200, -200)
t.pendown()
turtle.screensize(600, 600)
s = ''


# Compute:
for k in range(generation + 1):
    t.clear()   #clear screen
    s = add_to_string(work)
    printTurtle(s, t)   #print turtle
    s = ''  #re-init string

    time.sleep(1)

    #init new generation of work
    new = []
    for i in range(SIZE):
        row = [0] * SIZE
        new.append(row)
    #assign compute result to 'new'
    for i in range(SIZE):
        for j in range(SIZE):
            new[i][j] = compute(work, i, j)

    work = new

turtle.exitonclick()
