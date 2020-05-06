from operator import itemgetter

fruits = []     #list of fruit sublist
fruit_types = []    #list of fruit types

more = True
while more:     #while input
    fruit = input('Enter a fruit type (q to quit): ')
    if fruit == 'q':    #if q stop
        more = False
    else:
        weight = int(input('Enter the weight in kg: '))     #input weight
        if fruit in fruit_types:    #if fruit already exists
            for pair in fruits:
                if pair[0] == fruit:    #find fruit in fruit list
                    pair[1] += weight   #add weight

        else:   #if new fruiut
            l = [fruit, weight]
            fruits.append(l)        #add sublist
            fruit_types.append(fruit)   #add fruit type

fruits.sort(key=itemgetter(0))      #sort list

if len(fruits) == 0:
    print('No data recieved, exiting.')
else:
    for pair in fruits:
        print("{}, {}kg.".format(pair[0], pair[1]))


