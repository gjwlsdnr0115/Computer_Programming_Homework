# start of the output
n = 1

while n < 101:  # print until n reaches 100
    count = 0   # collumn count
    while count < 10:
        print(format(n, '>3'), end='')
        n += 1
        count += 1
    print()