weight=float(input(" Enter your weight in kg's= "))
height=float(input(" Enter your height in meter's= "))
BMI=round(weight/(height**2))
if BMI<18.5:
    print(f"your BMI is {BMI} and you are underweight.")
elif BMI<25:
    print(f"your BMI is {BMI} and you are normal.")
elif BMI<30:
    print(f"your BMI is {BMI} and you are overweight.")
elif BMI<35:
    print(f"your BMI is {BMI} and you are obese.")
else:
    print(f"your BMI is {BMI} and you are clinically obese.")
print("THANK YOU...")
