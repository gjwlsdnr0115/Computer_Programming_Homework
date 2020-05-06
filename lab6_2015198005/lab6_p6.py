more = True
while more:     #more input
    limit = int(input('Enter the limit L: '))   #input limit
    val = 0     #result value
    if limit == 0:      #if input 0 stop
        more = False
    else:
        for i in range(1, limit + 1):
            val += 1 / i    #add values until limit
        print('Sum of the initial', limit, 'term(s):', format(val, '.6f'))  #print value using 6 digits after the floating point
