class student:
    def __init__(self,m1):
           self.m1=m1
           #self.m2=m2

    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        else:
            return a
    def __str__(self):
        print(self.m1)




s1=student(10)
print(s1.sum(10,12,1))

print(s1.__str__())
