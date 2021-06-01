class a:
    cv=10

    def F1(self):
        #this.a=a
        #this.b=b
        print("Inside Method of Class",self.a,self.b)

    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("Inside Init",a,":)",b)


    def comp(self,a2) :
        if a1.a==a2.a:
            print("Both Values are Equal for a",a1.a)
        else:
            print("Both are different for a")
        if a1.b==a2.b:
            print("Its Equal",a1.b)
        else :
            print("different")



#    print("Inside Class")



a1=a("First variable",2)
a2=a("First variable",20)

a1.comp(a2)

a1.F1()
a2.F1()

a.cv=19
print(a1.cv,a2.cv)

a1.cv=11
a2.cv=15

print(a1.cv,a2.cv)

a.cv=19

a3=a(2,3)

print(a1.cv,a2.cv,a.cv,a3.cv)



