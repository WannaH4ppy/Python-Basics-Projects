def  factorial(n):
    #5! = 5 * 4 * 3 * 2 * 1
    result = 1
    for x in range(1,n+1):
        result *= x
    return result

print(factorial(5))
