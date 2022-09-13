import math

x = 3.251
y = 0.325
z = 0.466*10**-4
s = 0

e = 2.7182818

print(x,y,z)

numerator = 2**(y**x)
denominator = (3**x)**y
multiplier = y * (math.atan(z) - 1/3)
j = abs(x) + (1 / y**2 + 1)

s = numerator + denominator - multiplier / j

print(s)

#????????????????????????