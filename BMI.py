

def calculate_bmi(weight, height):
    """Calculate the Body Mass Index (BMI)."""
    return weight / (height ** 2)

def get_bmi_category(bmi):
    """Return the BMI category based on the BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Prompt the user for weight and height inputs
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate the BMI
bmi = calculate_bmi(weight, height)
category = get_bmi_category(bmi)

# Display the results
print(f"Your BMI is {bmi:.2f}.")
print(f"You are classified as: {category}.")
