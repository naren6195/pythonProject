# Filter map Reduce
from  functools import reduce
from Fibonoci import *
c=fib(10)


def f(n):
    return n%2==0



num=[1,2,3,4,5,6,7,8,9,10]

even= set(filter( lambda n : n%2==0,num))

oper1=list(map( lambda n : n%2==0,even))


oper=list(map( lambda n : n*2,even))

sum=reduce( lambda a,b   :    a+b,oper)

print(even,oper,oper1,sum)





print(__name__)