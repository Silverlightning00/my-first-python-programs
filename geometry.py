# This program contains functions that evaluate formulas used in geometry.
#
# Stephen Lee

import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

def parallelogram_area(b, h):
    a = b * h
    return a

def trapezoid_area(a, b, h):
    A = (a + b) / 2 * h
    return A

def rectangularprism_volume(l, w, h):
    v = w * h * l
    return v

def cone_volume(r, h):
    v = math.pi * r**2 * (h/3)
    return v
    
def sphere_volume(r):
    v = (4/3) * math.pi * r**3
    return v

def rectangularprism_surfacearea(l, w, h):
    A = 2 * ((w * l) + (h * l) + (h * w))
    return A

def sphere_surfacearea(r):
    A = 4 * math.pi * r**2
    return A

def hypotenuse_righttriangle(a, b):
    c = math.sqrt (a**2 + b**2)
    return c

# function calls
print(triangle_area(4,9))
print(circle_area(5))
print(parallelogram_area(5, 2))
print(trapezoid_area(10, 8, 4))
print(rectangularprism_volume(8, 4, 4))
print(cone_volume(7, 14))
print(sphere_volume(2))
print(rectangularprism_surfacearea(20, 10, 5))
print(sphere_surfacearea(5))
print(hypotenuse_righttriangle(5, 5))
