import sys
from math import sqrt, exp
a = float(sys.argv[1])
b = float(sys.argv[2])
x = sqrt(a*b)/(exp(a)*b)+a*exp(2*a/b)
print (x)