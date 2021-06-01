def gen():
    n=0
    yield 10
#    return 10
    while n<=10:
        sq=n*n
        yield sq
        n=n+1


c=gen()
#print(c)
print(c.__next__())



for i in c:
    print(i)

"""
1.COmpile Type error
2.Logical type
3.Run Tiime Error

"""

a=10
b=1

try:
    print(a/b)
    k=int(input())
    print(k)
except ValueError as c:
    print(c)
except ZeroDivisionError as c:
    print(c)
except Exception as c:
    print(c)


finally:
    print("Finally works :Which works even if we got an error in code")