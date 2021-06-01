for i in range(0,5,1):
    print('Hello world')

while i<=10:
    print(str(i))
    i+=1

s='String'

#print(s1)
for i in range(len(s)-1,-1,-1):
    print(s[i],end='')


for x in range(0,5):
    print(x,'Helllo WOrld')
    if x==4:
        break
    elif x==3:
        continue
        print(x ,' inside if loop')

x=range(3)
even=range(0,10,2)
print(x)
for i in x:
    print(i)
else:
    print('Else HIT in FOR LOOP')
for i in even:
    print(i)
while i<10:
    print(i)
    i+=1
else:
    print('Else hit in While Loop')