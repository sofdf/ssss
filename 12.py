import math
print("введите коэффиценты")
print("ax^2+bx+c=0:")
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))

d=b**2-4*a*c
print("дискриминант",d)
if d>0:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print(x1,x2)
elif d==0:
    x=-b/(2*a)
    print(x)
else:
    print("корней нет")