def is_Palindrome(s):
    '''
    A recursive function that returns whether input string is a palindrome
    :param s: input string
    :return: boolean result
    '''
    #stopping case 1
    if len(s) <= 1:     #string length is 1
        return True
    #stopping case 2
    if s[0] != s[len(s)-1]:     #first character and last character are not identical
        return False

    #recursive call of is_Palindrome()
    short_s = s[1:len(s)-1]     #make a substring by striping the first and last character
    return is_Palindrome(short_s)   #recursively call the function with the substring as input

#print welcome statement
print('This program can determine if a given string is a palindrome\n')
print('(Enter return to exit)')

#init boolean variable
more = True
while more:
    #user input
    chars = input('Enter string to check: ')

    if chars == '':
        more = False    #stop program
    else:
        #input has one letter
        if len(chars) == 1:
            print('A one letter word is by definition a palindrome\n')
        else:
            result = is_Palindrome(chars)

            if result:  #result is True
                print(chars, 'is a palindrome\n')
            else:   #result is False
                print(chars, 'is NOT a palindrome\n')

