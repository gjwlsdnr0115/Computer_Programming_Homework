base_str = input('What base? ')
base = int(base_str)
exp = int(input('What power of ' + base_str + '? '))
result = base ** exp
print('{} to the power of {} is {}'.format(base, exp, result))