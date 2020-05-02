# user input
num = int(input('Enter a number: '))

# initialize digit variable
digits = 0

# assign input into a new variable in order to save input information
num_count = num

count_digits = True
while count_digits:
    if num_count < 10:
        digits += 1
        count_digits = False
    else:
        num_count = num_count // 10
        digits += 1

if digits <= 1:
    print('The number {} contains {} digit'.format(num, digits))
else:
    print('The number {} contains {} digits'.format(num, digits))