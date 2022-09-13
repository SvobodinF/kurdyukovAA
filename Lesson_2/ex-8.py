
import math

x = -2.235*10**-2
y = 2.23
z = 15.221
s = 0

e = 2.7182818

print(x,y,z)

numerator = (e**abs(x-y)) * abs(x - y)**(x + y)
denominator = math.atan(x) + math.atan(z)
multiplier = (x**6 + math.log(y)**2)**(1/3)

s = numerator / denominator + multiplier

print(s)

