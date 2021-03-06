# Temperature Conversion Program (Celsius-Fahrenheit / Fahrenheit-Celsius)

# Display program welcome
print('This program will convert temperatures (Fahrenheit/Celsius)')
print('Enter (F) to convert Fahrenheit to Celsius')
print('Enter (C) to convert Celsius to Fahrenheit')

# Get temperature to convert
which = input('Enter selection: ')

while which != 'F' and which != 'C':
    which = input("Please enter 'F' or 'C': ")


if which == 'F':
    # Boolean variable to stop input loop
    invalid = True
    while invalid:
        temp = int(input('Enter temperature to convert: '))     # Requests input until valid temperature
        if temp >= -459.67:
            invalid = False                                     # if input is valid, loop stops
    converted_temp = format((temp - 32) * 5/9, '.1f')
    print(temp, 'degrees Fahrenheit equals', converted_temp, 'degrees Celsius')
else:
    invalid = True
    while invalid:
        temp = int(input('Enter temperature to convert: '))
        if temp >= -273.15:
            invalid = False
    converted_temp = format((9/5 * temp) + 32, '.1f')
    print(temp, 'degrees Celsius equals', converted_temp, 'degrees Fahrenheit')


