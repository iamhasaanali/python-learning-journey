def calculate_bmi(weight, height):
    bmi = weight/(height * height)
    return round(bmi, 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal weight"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"
    
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meter: "))

bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

print("Your bmi is", bmi)
print("Category", category)