#exercise 1

names = ["Hasaan", "Ali", "Sara"]
score = [85, 92, 78]

combined = zip(names, score)
student_dict = dict(combined)
print(student_dict)

#exercise 2
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])
print(matrix[1][2])

#exercise 3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item , end=" ")
    print()

#exercise 4 
person = {
    "name" : "Hasaan Ali",
    "age" : 28,
    "city" : "Sydney"
}
for key, value in person.items():
    print(f"{key} : {value}")