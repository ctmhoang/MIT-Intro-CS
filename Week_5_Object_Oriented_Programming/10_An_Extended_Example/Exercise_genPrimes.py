# Exercise: genPrimes
# 5/5 points (graded)
# ESTIMATED TIME TO COMPLETE: 10 minutes

# Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...



#None
def genPrimes():
    '''
    genPrimes, that returns the sequence of prime numbers
    on successive calls to its next() method: 2, 3, 5, 7, 11, ...
    '''
    listPrimes = [2]
    yield listPrimes[0]
    guess = 3
    while True:
        if all(guess % p != 0 for p in listPrimes):
            listPrimes.append(guess)
            yield guess
        else:
            guess += 1
