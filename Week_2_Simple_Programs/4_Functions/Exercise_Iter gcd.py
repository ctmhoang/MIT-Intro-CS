def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a == 0 or b == 0:
          print('GCD is ', max(a,b))
    else:
        def reducing(testval) :
            while a % testval != 0 or b % testval != 0:
                testval -= 1
            print('the greatest common divisor is ', testval)
        while True:
            if a > b:
                testval = b
                reducing(testval)
            elif b > a:
                testval = a
                reducing(testval)
            else:
                print('The greatest common divisor of both number is their value')
                break    
   
# Prof's Solution 
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    testValue = min(a, b)

    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue