def  factorial(n):
    #5! = 5 * 4 * 3 * 2 * 1
    result = 1
    for x in range(n):
        result *= x
    return result

#function above won't work properly as the range is implemented in wrong way
#it would multiply by 0 as the first element would be 0 (0,1,2,3,4) also
#the last element would be wrong as it's 4


def  factorial(n):
    #5! = 5 * 4 * 3 * 2 * 1
    result = 1
    for x in range(1,n):
        result *= x
    return result

#above function, would word half-way as the left range is correct, the right is
#wrong as we multiply be the last digit wich is 4, that leaves us with 24 instead of 120



def  factorial(n): #n is defined by the user
    #5! = 5 * 4 * 3 * 2 * 1
    result = 1 #starts from 1 & is multiplied by x which increments in ich loop
    for x in range(1,n+1): #correct range if n = 5, range is (1,2,3,4,5)
        result *= x #for n = 5, last iteration is result = result * x
                    #24 = 24 * 5, and that gives us 120
    return result

print(factorial(5))

#above everything is correct
