# Function to calculate BMI
def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

# Input from the user
weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight_kg, height_m)

# Display the result
print("Your BMI is:", bmi)

# Interpretation of BMI
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("Your weight is normal.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")