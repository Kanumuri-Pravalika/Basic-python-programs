vehicle=input("Enter the type of vehicle : ")
hours=int(input("Enter number of hours :"))
if vehicle=='truck'or'bus':
    charges=20*hours
    print("Your charges are : ",charges," per hour ")
elif vehicle=='car':
    charges=15*hours
    print("Your charges are : ",charges," per hour ")
elif vehicle=='Two wheeler':
    charges=10*hours
    print("Your charges are : ",charges," per hour ")
else:
    print("Invalid vehicle")
         
    