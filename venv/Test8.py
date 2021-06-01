import os

os.chdir("C:\\Users\\Narendra\\Desktop\\NewPythonTest")
print(os.getcwd())
f1=open('4567.txt','r+')
#f2=f1.read()
f3=f1.readlines()
f4=f1.readline()
#print(f3)
#print(f4)
for l in f3:
    print(l)

