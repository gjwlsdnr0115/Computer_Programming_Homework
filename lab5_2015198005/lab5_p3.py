# initialize integer list
int_list = []

# variable to stop while loop
more = True
while(more):
    num = int(input('Enter an integer: '))
    if(num > 100):  # input is larger that 100
        int_list.append('over')
    elif(num == 0):
        more = False    # no more input
    else:
        int_list.append(num)

print(int_list)
