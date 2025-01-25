#arithmetic operators
a=20
b=10
print(a+b)  #addition
print(a-b)  #subtraction
print(a*b)  #multiplication
print(a/b)  #division
print(a%3,b%3)  #modulus
print(a//3,b//3)  #floor division
print(a**2,b**3)  #exponents
print("")
#assignment operators
c=10
d=20
c+=30
d-=10
print(c)
print(d)
print("")
#comparison operators
e=10
f=20
print(e==f)  #equal to
print(e!=f)  #not equal to
print(e<f)   #les than
print(e>f)   #greater than
print(e<=f)  #less than or equal to
print(e>=f)  #greaer than or equal to
print("")
# logical operators
g=10
h=20
print(g!=h and g<h and g==h) #and operation
print(g==h or g<=h or g<h ) #or operation
print(not g>=h) #not operation
print("")
# membership operators
i="membership operators"
j=[1,2,3,4,5,6,7,8,9]
print('m' in i)
print(4 in j) # in operator
print('k' not in i) # not in operator
print("")
#identity operators
k=10
l=10
print(k is l,k==l) # is operator
print(k is not l,k!=l) # is not operator
print("")
#bitwise operators(binary operators)
m=10
n=12
print(bin(m))
print(bin(n))
print(bin(m&n),m&n) # binary AND operation
print(bin(m|n),m|n) # binary op operation
print(bin(m^n),m^n) # binary XOR operation
