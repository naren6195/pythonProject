import os
print(os.getcwd())
os.chdir("C:\\Users\\Narendra\\PycharmProjects\\pythonProject\\venv")

print(os.getcwd())

f=open('Name','r')
p1=open('COPY.JPG','wb')
f1=open('IELTS WR2 1.PNG','rb')
#f.write("Hello")
print(f1)
for i in f1:
    p1.write(i)

print(f)

f=open('Name','r')
for i in f:
    print(i)


print("Hello")