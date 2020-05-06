fraction = input('Enter a fraction: ')      #input fraction
short_fraction = ''     #initialize short string

for i in range(len(fraction)):
    if fraction[i] != ' ':              #if the character is not a blank
        short_fraction += fraction[i]   #add character
nums = short_fraction.split('/')    #split fraction
numerator = int(nums[0])        #numerator of fraction
denominator = int(nums[1])      #denominator of fraction
b = 0   #big num
s = 0   #small num
r = 0   #remainder
gcd = 0

if numerator > denominator:
    b = numerator
    s = denominator
else:
    b = denominator
    s = numerator

more = True
while more:     #while remainder is not 0
    r = b%s
    if r != 0:  #if remainder is not 0
        b = s
        s = r
    else:       #if remainder is 0
        gcd = s
        more = False

numerator = int(numerator / gcd)        #smallest numerator
denominator =int(denominator / gcd)     #smallest denominator

if denominator == 1:
    print('In lowest terms:', numerator)
else:
    print('In lowest terms: {}/{}'.format(numerator, denominator))