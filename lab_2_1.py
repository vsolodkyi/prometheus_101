import sys
from math import sqrt, exp, pi

x = float(sys.argv[1])
m = float(sys.argv[2])
q = float(sys.argv[3])

f = 1/(q*sqrt(2*pi))*exp(-(x-m)**2/(2*q**2))

#sqrt(a*b)/(exp(a)*b)+a*exp(2*a/b)
print (f)