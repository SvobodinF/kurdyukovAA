import math

x = 3.74*10**-2
y = -0.825
z = 0.16*10**2
s = 0

print(x,y,z)

numerator = 1 + math.sin(x + y)**2
denominator = abs(x - ((2 * y) / (1 + x**2 * y**2)))
multiplier = x**abs(y)
term = (math.cos(math.atan(1/z)))**2

s = numerator / denominator * multiplier + term

print(s)

