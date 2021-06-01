"""
#Duck Typing
class Laptop:
    def code(self,ide):
        print("inside Code Function of  LaptopClass")
        ide.execute()

class Editor:
    def execute(self):
        print("INside the class of EDitor class :)")

class pycharm:
    def execute(self):
        print("Inside the class of PPycharm")

i=pycharm()

a=Laptop()

a.code(i)
"""

#Operator Overloading
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
        print(m1,m2)

    def __add__(self, other):
        n1=self.m1+other.m1
        n2=self.m2+other.m2
        s3=Student(n1,n2)

    def __gt__(self, other):
        n1 = self.m1 + other.m1
        n2 = self.m2 + other.m2
        if n1>n2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)

s1=Student(10,12)
s2=Student(1,2)


s3=s1+s2


if s1>s2:
    print("S1 has More marks")
else:
    print("S2 has more marks")



a=10
print(a.__str__())

print(s1.__str__())



