#numeric data types
a=2
b=2.0
c=2+2j
print(a,type(a))  # integers
print(b,type(b)) #float
print(c,type(c)) # complex numbers
print("")
#sequence data types
d=[1,2,3,'list']  #list(mutable)
e=(1,2,4,'tuple')  #tuple(immutable)
f={
    'subject name' : 'python',
    'duration': '6months'
}  #dictionary (mutable)
g={1,1,1,1,2,3,4,5,"set"}  # immutable
print(d,type(d))
print(e,type(e))
print(f,type(f))
print(g,type(g))
print("")
#userinput and casting types
a1=int(input("enter the 1st value:-"))
a2=int(input("enter the 2nd value:-"))
print(a1+a2)                          #int (casting type)
print("")
a3=float(input("enter the 1st value:-"))
a4=float(input("enter the second value:-"))
print(a3+a4)                         #float(casting type)
print("")
a5=eval(input("enter the 1st value:-"))
a6=eval(input("enter the 2nd value:-"))
print(a5+a6)                        #eval(casting type)
print("")

