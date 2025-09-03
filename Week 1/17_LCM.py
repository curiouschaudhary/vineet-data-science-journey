import math

def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)
print(lcm(4, 6))