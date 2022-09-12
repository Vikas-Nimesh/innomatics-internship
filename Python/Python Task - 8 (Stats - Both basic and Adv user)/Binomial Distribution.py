import math


p1 = 1.09
p = p1/(p1+1)
q = 1-p
n = 6
R = []
for x in range(3,7):
    c1 = math.factorial(n)/(math.factorial(x)*(math.factorial(n-x)))
    c2 = p**x
    c3 = q**(n-x)
    res = c1*c2*c3
    R.append(res)
re = sum(R)
print(round(re, 3))