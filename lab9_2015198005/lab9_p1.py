import stack

def match(left, right):
    '''
    Returns whether the two input parentheses/braces match
    :param left: left parentheses/brace
    :param right: right parentheses/brace
    :return: boolean value
    '''
    if left == '(':
        if right == ')':    #match
            return True
        else:
            return False
    elif left == '{':
        if right == '}':    #match
            return True
        else:
            return False
    else:   # left input is not parentheses/brace
        return False

#user input
inp = input('Enter parentheses and/or braces: ')

#initialize boolean variable
is_proper = True
#create stack
s = stack.getStack()

for c in inp:   #for each character in input string
    if c == '(' or c == '{': #left parentheses/braces
        stack.push(s, c)
    else:         #right parentheses/braces
        item = stack.pop(s)
        if item == None:    #stack is empty
            is_proper = False
            break           #break for loop
        else:   #stack not empty
            if not match(item, c):  #if doesn't match
                is_proper = False
                break       #break for loop

if not stack.isEmpty(s):    #if stack is not empty
    is_proper = False

#print result
if is_proper == True:
    print('Nested properly.')
else:
    print('Not properly nested.')
