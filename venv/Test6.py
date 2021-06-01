import calendar
import os

x,y,z=map(int,input().split())
print(x,y,z)
#print(list(x))

print(os.getcwd())
file =open('TEST1.py','r')
file.close()
os.chdir("C:\\Users\\Narendra\\Desktop\\NewPythonTest")
print(os.getcwd())
os.mkdir("NewPythonTest1")
os.chdir("NewPythonTest1")
print(os.getcwd())