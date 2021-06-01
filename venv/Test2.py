a=(1,2,3,4,5)
a1=(2,3,4)
b=list(a)
b[0]=-1
print(a[:],b)
print(a+a1)
for i in range(len(a)):
    print(a[i])

#Dictionaries


di=dict()
print(di)
di={1:10,2:20,3:30}
di2=list(di)
print(di.get(1))
di.pop(1)
for i in di.keys():
    print(i)

for i in di.values():
    print(i)
#    print(di.get(i))


#Sets

s={1,2,3,"a"}
s1={"a","b",1,2}
print(s)
s.add(1)
print(s)
s.remove(1)
print(s)
s.discard(2)
print(s)
print(s.difference(s1),s1,s)
print(s.intersection(s1))
print(s.union(s1))

X=None
if X is None:
    print(X)
