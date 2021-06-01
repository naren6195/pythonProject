def fib(num):
    first=0
    second=1
    l=[0,1]
    if num==0 or num==1:
        return l[num]
    else :
        for i in range(2,num):
            l.append(first+second)
            first=second
            second=l[i]
    return l[num-1]

print(fib(10))
print("Hello", __name__ )


