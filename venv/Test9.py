import  os
os.getcwd()
os.chdir("C:\\Users\\Narendra\\Desktop\\NewPythonTest")
print(os.getcwd())
f=open("4567.txt","a")
f.write("\nAdded from Pycharm")
f.writelines(["\nWrite Lines from1 ","\nWrite Lines from 2","\nWrite Lines from 3"])
f.close()




S, sub = input(),input()
count = 0

while sub in S:
    i = S.find(sub)
    print(i)
    print("S[:i] : ",S[:i],"S[i + 1:]:",S[i + 1:])
    S = S[:i] + S[i + 1:]
    count += 1

print(count)