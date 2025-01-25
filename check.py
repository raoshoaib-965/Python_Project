#string indexing and slicing
from html.parser import charref
from itertools import chain

b2="welcome to pakistan"
print(b2[8])
b2="biaohs olleh"
print(b2[-1::-1])
print()
#string iteration
s="welcome to pakistan"
d=len(s)
print(d)
for a in range(d):
    print(s[a])
#string functions
f="hello world"
t=f.lower()   #lower
print(t)
print()
y=f.upper()   #upper
print(y)
print()
i=f.title()   #title
print(i)
print()
p=f.capitalize()   #capitalize
print(p)
print()
h="hello"
print(h.find("c"))
print(h.index("l"))
print(h.isalnum())
print(h.isalpha())
print(h.isdigit())
#char & ord function
f=78
print(chr(f))
f="Z"
print(ord(f))
print()
#string formatting
u="{a:5} my name is {b:7}".format(a="hello",b='shoaib')
print(u)
print()
#list slicing
w=[3,6,9,0,1,2,65,"hello"]
print(w[1::2])
print()
#list iteration
f=[5,7,8,3,5,6,'world']
r=len(f)
for q in range(r):
    print(f[q])
print()
#list comprehension
y=[r for r in range(1,101,2)]
print(y)
u="hello my name is shoaib"
w=[q for q in u]
print(w)
print()
#list functions
f=[20,80,50,60,90]
del f[4]
print(f)
print()
#pop function
f.pop(1)
print(f)
print()
#rmove function
f=[30,90,60,50,60]
f.remove(90)
print(f)
print()
#insert function
t=[40,90,6,5,2,4]
t.insert(4,30)
print(t)
print()
#append function
e=[4,7,8,7,6,5,5,5]
d=[6,78,86,5,5,4]
e.append(d)
print(e)
print()
#extend function
e.extend(d)
print(e)
print()
#count function
g=[2,2,2,2,2,2,4,5,6,7,8,9]
t=g.count(2)
print(t)
print()
#max function
h=[1,2,3,4,5,6,7,8,9]
t1=max(h)
print(t1)
print()
#min function
s=[9,8,7,6,5,4,3,2,1]
m=min(s)
print(m)
print()
#sort function
p=[5,8,2,7,0,1,5,8,9]
j=sorted(p)
print(j)
print()
#reverse function
o=[9,8,7,6,5,4,3,2,1]
o.reverse()
print(o)
print()
#index function
g=[5,7,8,9,0,1,4]
k=g.index(9)
print(k)