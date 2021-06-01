a='single quote'
b=" double quotes"
c='''3 single quotes'''
'''
comment section
'''

d="""Narendra"""
e='Helllalalalal alalal a a a'
d=d.upper()
d=d.title()
print(a,    b,  c,   d)
print(d[0:len(d)])

if d.startswith('n'):
    print(bool(True))
if d.endswith('a'):
    print(bool(False))

print(d.upper())
print(d.lower())
print(d.isupper())

print(d.capitalize())
''' capitalises the first letter of String'''

print(e.title())

p=10
st='the price of car is {}'
print(st.format(p))

print(st.replace('the','hello,'))
i='1112'
int=[1,2,3,4,5,56,66]
set=['a','b','c','d','1']
f='-'.join(set)
print(f)
print(d.find('x'))
print(d.isspace())
print(i.isnumeric())
'''--- if any character is numeric it returns true'''
print(i.isdigit())
''' return true if every charater is numeric'''

def name(n):
    print("hello"+' '+n)

name('Narendra')
name('Jayanth')