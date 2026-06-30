numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
print(doubled)

even_only = [n for n in numbers if n % 2 == 0]
print(even_only)