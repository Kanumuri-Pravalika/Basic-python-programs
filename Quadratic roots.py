import math
a=float(input("Enter a :"))
b=float(input("Enter b :"))
c=float(input("Enter c :"))
d=b*b-4*a*c
if d>0:
    root1=(-b+math.sqrt(d))/2*a
    root2=(-b-math.sqrt(d))/2*a
    print("Two distinct and real roots :")
    print("Root 1 : ",root1)
    print("Root 2 : ",root2)
elif d==0:
    print("Roots are equal : ")
    root=-b/2*a
    print("Root :",root)
else:
    real=-b/2*a
    imag=math.sqrt(-d)/2*a
    print("Roots are imaginary ")
    print("Root 1:",real,"+",imag,"i")
    print("Root 2:",real,"-",imag,"i")