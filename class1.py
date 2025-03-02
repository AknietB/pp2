class Answer:
    def __init__(self):
        self.userstr = '' 

    def getstring(self):
        self.userstr = input()  

    def printstring(self):
        print(self.userstr.upper())  

ans = Answer()  
ans.getstring()  
ans.printstring()  
