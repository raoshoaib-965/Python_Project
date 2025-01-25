#del function in list(index number)
from itertools import count

l=[1,2,3,4,5,6,7]
del l[3]
print(l)

print("")
#pop function in list(works on index number)
p=[2,3,4,5,6,7,8]
p.pop(6)
print(p)
print("")
# remove list function(works on list number)
z=[3,4,5,6,7,8,9]
z.remove(5)
print(z)
print("")
#update list function(index number)
c=[2,3,7,9,3,5,8]
c[2]=9
print(c)
print("")
#insert list function
v=[3,2,5,72,3,7]
v.insert(5,2)
print(v)
print("")
# append list function
b=[53,63,65,75,23,64,75]
b.append(32)
print(b)
print("")
# extends list function
n=[43,56,778,87,56,7,876]
t=[45,676,87,998]
n.extend(t)
print(n)
print("")

# count list function
f=[3,4,5,6,7,8,8,9,9,8,7,7,6,6,5,5,4,33,33,3,3,3,3,3,3]
g=f.count(3)
print(g)
print("")
# max list function
h=[45,6,7,8,8,9,3,4,3,4,5,5,6,6]
r=max(h)
print(r)
print('')
#min list function
t=[1,23,4,5,6,7,8]
e=min(t)
print(e)
print('')
# sort list function
d=[9,8,7,6,6,5,4,4,3,2,1]
q=sorted(d)
print(q)
print('')
#reverse list function
a=[1,2,2,3,4,5,6,7,8,9]
a.reverse()
print(a)
print('')
#index list function
y=[5,2,4,5,6,7]
j=y.index(4)
print(j)
