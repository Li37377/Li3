# #
# Write a Python program to calculate the Body Mass Index (BMI) and categorize it based on the calculated value using conditional statements.

# The program should:

# Prompt the user to enter their weight in kilograms.
# Prompt the user to enter their height in meters.
# Calculate the BMI using the formula:
# BMI=weight/height^2
# Categorize the BMI based on the following criteria:
# Underweight: BMI < 18.5
# Normal weight: 18.5 ≤ BMI < 24.9
# Overweight: 25 ≤ BMI < 29.9
# Obesity: BMI ≥ 30
# Display the calcul


w=float(input("Enter your weight in kilograms"))
h=float(input("enter your height in meters"))

BMI=w/(h**2)
if BMI < 18.5:
   print("underweight",BMI)
elif 18.5<=BMI<24.9:
    print ("normal",BMI)
elif 25<=BMI<29.29:
    print ("overweight",BMI)
elif BMI > 30:
    print("obesity",BMI)
    

