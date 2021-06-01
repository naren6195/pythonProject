class Student:
    def __init__(self):
        self.num=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return  val
        else:
            raise StopIteration

val=Student()

print(next(val))
#print(iter(i))

print(val.__next__())

for i in val:
    print(i)
    