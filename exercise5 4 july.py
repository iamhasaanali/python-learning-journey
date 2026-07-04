temperatures = [22, 35, 18, 40, 28, 15, 33, 27]
high_temp = [temp for temp in temperatures if temp > 25]
conveert_temp = [((temp * 9/5) + 32) for temp in temperatures]

print("High temperatures (above 25°C):", high_temp)
print("Converted temperatures to Fahrenheit:", conveert_temp)