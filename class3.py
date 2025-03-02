class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self , a , b):
        super().__init__()
        self.a = a
        self.b = b
    def area(self):
        return self.a *self.b
answer = Shape()
a = int(input("Your a: "))
b = int(input("Your b: "))
print("defoult area: " , answer.area())
inp_ar = Square(a , b)
print("your area: " , inp_ar.area())