# 4- BMI calculator : create a python function that takes the user
# height , weight and print the user BMI and if the user underweight ,
# overweight or healthy


# pip install body-mass-index
from bmi import Bmi

# Code with a package
# inputs
while True:
    try:
        height, weight  = float(input("Please input Height(m): ")), float(input("Please input Weight(kg): "))
        break
    except Exception:
        print("Error: Please type again a valid numbers.")

# calc BMI
BMI = Bmi.calculate_bmi(weight,height)
print(f"BMI = {BMI}")
print(f"You are: {Bmi.get_bmi_range_info(BMI)}")




# My Normal Solution Code

'''
BMI = weight/height**2
print(f"BMI = {BMI}")

if BMI <= 18.4: 
    print("You are : Underweight")
elif BMI <= 24.9: 
    print("You are : Normal")
elif BMI <= 39.9:  
    print("You are : Overweight")
else: 
    print("You are : Obese")

'''
