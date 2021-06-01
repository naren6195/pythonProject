def Hello():
    print("Hello_world")

Hello()
x=1
y='Narendr'
print(x,y)
if x>1:
    print("X is greater then 1")
elif x<1:
    print('x is less than one')
elif x==1:
    print('Fucker')

Lett =[1,'a','b',30]
Let=(1,12,'a','am')
for x in 'Lett':
    print(x)
for x in Let:
    print(x)
nu=1
while nu<10:
    nu+= 1
    print(nu)


def global_variable():
    global t
    t=10

global_variable()
z=nu+t
t+=10
print('z values is=',z,"t value", t)
b="10 String"
c="Sitring"
a="10" not in b
print(a)
while a!=True:
    print (a)
    a=not a
print(float(2//1))
a=2.211
b=1
print(float(a+b))
c=str(a+b)
print(bool(["a","b","c"]))

ab=[9,1,2,3,4,5,6]
print(len(ab))

for i in range(len(ab)):
    print(ab[i])

if 30 in ab:
    print ("its in the list")
else :
    print("its not in the list")

ab=[9,1,2,3,4,5,6]
ab.append(7)
print(ab)
ab.sort()
print(ab)
ab.remove(9)
print(ab)
ab.reverse()
print(ab)
ab2=ab
ab.extend(ab2)
print(ab)
ab.sort()
print(ab)
ab.insert(1,10)
print(ab)
ab.pop(6)
print(ab)
print(ab.count(1))
ab.remove(1)
print(ab)
print(ab.count(1))
ab.clear()
print(ab)
