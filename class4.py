class Point():
    def __init__(self):
        pass
    def inp(self , x , y):
        self.x = x
        self.y = y
    def show(self):
        print("Point coordinates: " , self.x , self.y)
    def move(self , dx , dy):
        self.x += dx
        self.y += dy
    def dist(self , x_other , y_other):
        print(((self.x - x_other)**2 + (self.y - y_other)**2)**0.5)
answer = Point()
x = int(input("Your x: "))
y = int(input("Your y: "))
answer.inp(x , y)
answer.show()
dx = int(input("Your dx: "))
dy = int(input("Your dy: "))
answer.move(dx , dy)
x_other = x
y_other = y