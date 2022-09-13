import math

x = 3.981*10**-2
y = -1.625*10**3
z = 0.512
s = 0

e = 2.7182818

print(x,y,z)

numerator = 2**-x
denominator = math.sqrt(x + abs(y)**(1/4))
multiplier = (e**(x - 1 / math.sin(z)))**(1/3)

s = numerator * denominator * multiplier

print(s)

