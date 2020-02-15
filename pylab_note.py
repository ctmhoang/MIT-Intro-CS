#This code shows the very basics of creating arrays and using them

import pylab

#Array of ints
a = pylab.array([1,4,5,8])
print a
print type(a)

#Array of floats
b = pylab.array([2,3,7,9], float)

#Can do math on the arrays very easily, which we couldn't do with lists
c = a * 2 + 10
print c

d = a * b
print d

#Can even do element-wise operations like sine:
print pylab.sin(d)

#Like lists, arrays can be sliced and mutated
print d[1:]

d[0] = 1000
print d

#Add elements to an array using the append function
d = pylab.append(d,[1,2,3])
print d

#It is more efficient to create arrays of a large size at once rather than
#increasing its length in steps. To create a matrix of zeros or ones:
e = pylab.zeros((2,3))
f = pylab.ones((2,3))

#To change the element of f at row 2 and column 1 to 5 we would write:
f[1,0] = 5;
print f

#To change the whole second row to 10, we could write:
f[1,:] = 10
print f


#Other useful functions are arange and linspace. arange returns an array
#with regularly incremented values. linspace returns an array with a
#specified number of elements between beginning and end values

print pylab.arange(2,3,0.1)
print pylab.linspace(1.0,4.0, 6)
