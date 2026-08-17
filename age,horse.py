height=float(input("Enter your height in feets: "))
if height>3:
    print("You can ride on the horse : ")
    age=int(input("Enter your age : "))
    if age<=12:
        print("You ticket price is : 150")
    elif age>13 and age<=18:
        print("Your ticket price is : 250")
    else:
        print("Your ticket price is : 500")
else:
    print("You cannot ride on the horse ")
    print("..........Thank you..........")