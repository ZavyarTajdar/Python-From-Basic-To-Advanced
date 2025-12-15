import math

def circleStats(rad):
    area = math.pi * rad ** 2 
    circumference = 2 * math.pi * rad
    return area, circumference

print(circleStats(2))