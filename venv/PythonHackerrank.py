a='Narendra12'
b=[]
#b.insert(0,a[:4])
#b.insert(1,a[:4])
#for i in a:
 #   b+=i
for i in range(0,int(len(a)),4):
    b.insert(i,a[i:i+4])

#'''if i*2<len(a):
#    print(a[i*2+1:])
#print(i)
#'''
for m in b:
    print(m)


