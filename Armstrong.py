n=int(input("Enter any integer : "))
a=0
m=n
while n!=0:
    rem=n%10
    a=a+rem*rem*rem
    n=n//10
if a==m:
    print(m,"is an armstrong number")
else:
    print(m,"is not an armstrong number")