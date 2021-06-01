class Student:
    company="Wells Fargo"

    def __init__(self,name,age,cell):
        self.name=name
        self.age=age
        self.cell=cell
        self.b1= self.b()

    @classmethod
    def class_meth(cls):
        print("Class Method",Student.company)


    @staticmethod
    def info(deta):
        print("Static method not utilisng obejects ",deta)

    class b:
        def __init__(self):
            self.x=1
            self.y=2
        def show(self):
            print(self.x,self.y)


s1=Student("Narendra",26,9501911438)
s2=Student("Kiran",25,8499981920)


#print(s1.name,s1.age,s1.cell)
#print(s2.name,s2.age,s2.cell)

print(s1.class_meth())
print(s1.info("Hahah"))

l1=s1.b()
l1.show()