import math
def area_trapezoid(height,base1,base2):
    return (1/2)*(base1+base2)*height
height=int(input("height:"))
base1=int(input("base1:"))
base2=int(input("base2:"))
print(area_trapezoid(height,base1,base2))