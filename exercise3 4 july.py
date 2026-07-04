def temperature_converter(temp, unit):
    if unit == "C":
        converted_temp = (temp * 9/5) + 32
        return f"{temp}°C is equal to {converted_temp}°F"
    elif unit == "F":
        converted_temp = (temp - 32) * 5/9
        return f"{temp}°F is equal to {converted_temp}°C"
    else:
        return "Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit."
    
t1 = temperature_converter(25, "C")
t2 = temperature_converter(77, "F")
t3 = temperature_converter(100, "X")  
print(t1)
print(t2)
print(t3)