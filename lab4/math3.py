import math
def area_poligon(sides, length):
    return (sides*length**2)/(4*math.tan(math.pi/sides))
sides=int(input("number of sides:"))
length=int(input("length of sides:"))
print(area_poligon(sides, length))