def calculate_bmi(weight,height):
    return round (weight / (height * height), 2)
def bmi_message(weight,height):
    bmi= calculate_bmi(weight,height)
    if bmi < 18.5:
        return "Underweight"
    elif bmi <25:
        return "Normal"
    elif bmi <30:
        return "Overweight"
    else:
        return "Obese"

print(bmi_message(70,1.72))