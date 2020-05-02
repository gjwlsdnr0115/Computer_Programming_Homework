# user input
income = int(input('Enter the taxable income in USD: '))

# initializing tax variable
tax = 0

if income <= 750:
    tax = income * 0.01
elif income <= 2250:
    tax = (income - 750) * 0.02 + 7.50
elif income <= 3750:
    tax = (income - 2250) * 0.03 + 37.50
elif income <= 5250:
    tax = (income - 3750) * 0.04 + 82.50
elif income <= 7000:
    tax = (income - 5250) * 0.05 + 142.50
else:
    tax = (income - 7000) * 0.06 + 230.00

# print result using 2 digits precision after the fractional point
print('Tax due:', format(tax, '.2f'), 'USD')