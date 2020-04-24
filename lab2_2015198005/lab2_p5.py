print('This program will convert degrees Celsius to degrees Fahrenheit')

celsius = float(input('Enter degrees Celsius: '))
fahren = celsius * 9/5 + 32


print(celsius, 'degrees Celsius equals',
      format(fahren, '.1f'), 'degrees Fahrenheit')
