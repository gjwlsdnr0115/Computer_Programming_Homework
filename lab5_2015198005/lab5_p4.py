# user input
height = int(input('Enter an integer: '))
width = 2 * height - 1
# number of blanks before printing line
blank = 0

while(height > 0):
    print(' '*blank + '*'*width)
    height -= 1     # decrease height
    width = 2 * height - 1  # update width to match height
    blank += 1      # increase blank