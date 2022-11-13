class Add():
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print (self.num1 + self.num2)
class Sub():
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2
    def sub(self):
        print (self.num1 - self.num2)
class Mul():
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2
    def mul(self):
        print (self.num1 * self.num2)
class Truediv():
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2
    def truediv(self):
        print (self.num1 / self.num2)
class Calc(Add,Sub,Mul,Truediv):
    ...
num1 = Calc(40,20)
num2 = Calc(20, 15)
num3 = Calc(4, 5)
num4 = Calc(60,12)
num1.add()
num2.sub()
num3.mul()
num4.truediv()
