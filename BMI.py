height=float(input("Enter your height in meters : "))
weight=float(input("Enter your weight in kilograms : "))
bmi=weight/height*height
BMI=round(bmi)
print("BMI=",bmi)
print("Your health condition is :")
if BMI<18.5:
    print("Under weight")
elif BMI>18.5 and BMI<25:
    print("Normal weight")
elif BMI>25 and BMI<30:
    print("Overwight")
elif BMI>30 and BMI<35:
    print("Obese")
else:
    print("Consult a doctor immeadiately ")
        