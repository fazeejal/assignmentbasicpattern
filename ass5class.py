##1

class MyString:
    def __init__(self,s):
        self.s = s
    def get_str(self):
        return self.s
    def get_upper(self):
        return self.s.upper()
ms=MyString("hello world")
og=ms.get_str()
print("original string is : ",og)
ug=ms.get_upper()
print("uppercase : ",ug)

##2


class ClassPara:
    classparameter="my class"
    def __init__(self,instanceparameter):
        self.instanceparameter=instanceparameter
ob=ClassPara("ins 1")
ob1=ClassPara("inst2")
print("class parameter is :",ob.classparameter)
print("instance parameter 1 is : ",ob.instanceparameter)
print("instance parameter 2 is : ",ob1.instanceparameter)

#3

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
c=Circle(2)
result=c.area()
print("area of cicle is : ",result)

#4
class Account:

    def __init__(self,bal=0):
        self.bal=bal
    def deposit(self,ammount):
        self.ammount=ammount
        if self.ammount > 0:
            self.bal =+ ammount
            print("balance is ",self.bal)
        else:
            print("deposite a valid ammount")
    def withdraw(self,ammount1):
        self.ammount1=ammount1
        if self.ammount1 > 0:
            self.bal = self.bal- ammount1
            print("balance is ",self.bal)
        else:
            print("zero ammount is withdrawn")
acc=Account()
acc.deposit(200)
acc.withdraw(10)

#5

class Shape:
    def area(self):
        return 0  

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2  


shape = Shape()
print("Area of Shape:", shape.area())  

square = Square(5)
print("Area of Square:", square.area())




        
