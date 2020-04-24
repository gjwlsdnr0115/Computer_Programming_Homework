
print('Welcome to the SETI program')
print('This program will allow you to enter specific values related to')
print('the likelihood of finding intelligent life in our galaxy. All')
print('percentages should be entered as integer values, e.g., 40 and not .40')
print()

p = 100
n = int(input('How many planets per star do you think can support life?: '))
f = 100
i = 100
c = 100
L = int(input('How long do you think civilizations on other worlds last?: '))

num_detectable_civilizations = 7 * (p/100) * n * (f/100) * (i/100) * (c/100) * L

print()
print('Based on the values entered ...')
print('there are an estimated', num_detectable_civilizations,
       'potentially detectable civilizations in our galaxy')

