import os

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = float(weight/(height*height))
bmi2 = round(bmi)

if bmi > 35:
  print(f"Your BMI is {bmi2}, you are clinically obese.")

elif bmi > 30 and bmi < 35:
  print(f"Your BMI is {bmi2}, you are obese.")

elif bmi > 25 and bmi < 30:
  print(f"Your BMI is {bmi2}, you are slightly overweight.")

elif bmi > 18.5 and bmi < 25:
  print(f"Your BMI is {bmi2}, you have a normal weight.")

else:
  print(f"Your BMI is {bmi2}, you are underweight.")

os.system('pause')