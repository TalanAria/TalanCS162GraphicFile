import numpy as np

#Use Numpy to generate a random 2-dimensional numpy array with dimensions 5x5
array = np.random.randint(0,15, size=(5,5), dtype=int)

#Print the entire array.
print(array)

#Print the number from the 2nd row, 3rd column
print(f"row 2{array[1]},row 3{array[2]}")

#Print the sum of all the elements in the array.
print(f" sum of all elements in the array is {np.sum(array)}")

#the mean of each row in the array.
print(f"the mean of each row {np.mean(array, axis=1)}")

#Print the maximum value in each column of the array.
print(f"maximum value in each column of the array {np.max(array, axis=1)}")
