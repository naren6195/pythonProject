class C:
    def __init__(self):
        print("In INIT of C")

class A:
    def __init__(self):
        print("Inside INITI Of CLASS A")

    def f1(self):
        print("Feature 1")

    def f2(self):
        print("Feature 2")

class B(A,C):
    def __init__(self):
        super().__init__()
        super().f2()
        print("Inside INITI Of CLASS B")
    def f3(self):
        print("Feature 3")
    def f4(self):
        print("Feature 4")


a1=B()

