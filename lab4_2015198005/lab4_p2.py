# sum of input
sum = 0

# boolean variable to stop loop
stop = False
while stop == False:
    num = int(input('Your number: '))
    if num <= 100:
        sum += num
    if num == 0:
        stop = True

print('Sum:', sum)