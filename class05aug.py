import numpy as np
numbers = np.array([1,2,3,4,5])

print(numbers)
print(type(numbers))
print(numbers.dtype)
print(numbers * 2)
print(numbers + 10)    
print(numbers ** 2)    
print(numbers > 3)
print("-------------------------------")
#exercise 2
import numpy as np

numbers = np.array([15, 8, 23, 4, 42, 16, 7])

print(np.sum(numbers))
print(np.mean(numbers))
print(np.max(numbers))
print(np.min(numbers))
print(np.std(numbers))
print(np.sort(numbers))
print("-------------------------------")

#exercise 3

import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(matrix)
print("shape:", matrix.shape)
print("rows:", matrix.shape[0])
print("columns:", matrix.shape[1])
print("-------------------------------")
print(matrix[0])      # first row
print(matrix[1])      # second row
print(matrix[0][2])   # first row, third item
print(matrix[1][1])   # second row, second item
print("-------------------------------")
print(np.sum(matrix))           # total of ALL numbers
print(np.sum(matrix, axis=0))   # sum of each COLUMN
print(np.sum(matrix, axis=1))   # sum of each ROW
print(np.mean(matrix, axis=0))  # mean of each COLUMN
print(np.mean(matrix, axis=1))  # mean of each ROW
print("-------------------------------")

#exercise 4
import numpy as np
scores = np.array([
    [85, 92, 78],
    [90, 65, 88],
    [72, 95, 83]
])
print(scores.shape)
print(np.sum(scores))
print(np.mean(scores, axis = 0))
print(np.mean(scores, axis = 1))
print(np.max(scores))
print(np.sort(scores[0]))
