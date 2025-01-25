#conditional statements
a=int(input("enter the value:-"))
if a>=85:
    print("4")
elif a>=70:
    print("3")
elif a>=50:
    print("2")
else:
    print("fail")
#basic calculator
a1=int(input("enter the 1st number:-"))
a2=int(input("enter the 2nd number:-"))
a3=input("enter the opr(+,-,*,/):-")
if a3=="+":
    print(a1+a2)
elif a3=="-":
    print(a1-a2)
elif a3=="*":
    print(a1*a2)
elif a3=="/":
    print(a1/a2)
else:
    print("invalid opr")
print()
#loops
# for loop
for a7 in range(1,11,1):
    print("5","","*",a7,"=",5*a7)
    print()
#while loop
b1=1
while b1<=10:
    print(b1,"while loop")
    b1=b1+1
print()
#string indexing and slicing
b2="welcome to pakistan"
print(b2[8])


