# initialize largest number variable
largest_num = 0

# variable to stop while loop
more = True
while(more):
    num = float(input('Enter a number: '))
    if(num > largest_num) :
        largest_num = num
    if(num == 0):
        more = False

if(largest_num > 0):    # if there was a positive number input
    print('The largest number entered was', format(largest_num, '.2f') )
else:
    print('No positive number was entered')