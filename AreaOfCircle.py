'''Write a Python program which accepts the radius of a circle from the user and compute the area.'''

from math import pi
radius = float(input('Enter radius of circle: '))
AreaOfCircle = (pi*radius*radius)
print(f'Area of given circle with radius {radius} is: {AreaOfCircle}')