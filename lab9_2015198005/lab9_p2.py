import sys
import stack

def is_Operator(c):
    '''
    Returns whether character is an operator
    :param c: input character
    :return: boolean result
    '''
    if c == '*' or c == '/' or c == '+' or c == '-' or c == '=':    #is an operator
        return True
    else:
        return False

#intialize boolean variable
more = True
while more: #input not 'q'
    inp = input('Enter an RPN expression: ')
    if inp == 'q':  #quit program
        more = False
    elif inp == '':
        print('Evaluation error')
        sys.exit(1)
    else:
        #split list by ' '
        inp_list = inp.split()

        #convert operands into float
        for i in range(len(inp_list)):
            if not is_Operator(inp_list[i]):
                inp_list[i] = float(inp_list[i])
        #make stack
        s = stack.getStack()

        #intialize evaluation result variable
        evaluation = 0

        #evaluate expression
        for c in inp_list:
            #is an operator
            if is_Operator(c):
                if c == '=':
                    evaluation = stack.pop(s)
                    if evaluation == None:  #stack is empty
                        print('Evaluation error')
                        sys.exit(1) #exit program
                elif c == '*':
                    o2 = stack.pop(s)
                    o1 = stack.pop(s)
                    if o1 == None or o2 == None:    #stack underflow
                        print('Evaluation error')
                        sys.exit(1) #exit program
                    result = o1 * o2
                    stack.push(s, result)
                elif c == '/':
                    o2 = stack.pop(s)
                    o1 = stack.pop(s)
                    if o1 == None or o2 == None:    #stack underflow
                        print('Evaluation error')
                        sys.exit(1)
                    if o2 == 0:
                        print('Evaluation error')   #divide by 0
                        sys.exit(1)
                    result = o1 / o2
                    stack.push(s, result)
                elif c == '+':
                    o2 = stack.pop(s)
                    o1 = stack.pop(s)
                    if o1 == None or o2 == None:    #stack underflow
                        print('Evaluation error')
                        sys.exit(1)
                    result = o1 + o2
                    stack.push(s, result)
                else:
                    o2 = stack.pop(s)
                    o1 = stack.pop(s)
                    if o1 == None or o2 == None:    #stack underflow
                        print('Evaluation error')
                        sys.exit(1)
                    result = o1 - o2
                    stack.push(s, result)

            #is an operand
            else:
                stack.push(s, c)

        #stack is not empty
        if not stack.isEmpty(s):
            print('Evaluation error')
            sys.exit(1)

        if float.is_integer(evaluation):    #if result is integer, convert to integer and print
            print('Value of expression:', int(evaluation))
        else:   #print with two digits after fractional point
            print('Value of expression:', format(evaluation, '.2f'))
