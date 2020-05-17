def evalPolynomial(x):
    """
    Computes the polynomial with the given input x
    :param x: value to compute polynomial
    :param result: computation result
    :return: computation of the polynomial
    """
    result = 3*x**5 + 2*x**4 - 5*x**3 - x**2 + 7*x - 6
    return result

value  = int(input("Enter a value for x: "))      #input value
print('Polynomial for x='+str(value)+': '+str(evalPolynomial(value)))   #print result, casting integer value into string