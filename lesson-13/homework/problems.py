import numpy as np

# Task 1: 
vector = np.arange(10, 50)
print("Vector with values ranging from 10 to 49:")
print(vector)

# Task 2: 
matrix_3x3 = np.arange(9).reshape(3, 3)
print("\n3x3 matrix with values ranging from 0 to 8:")
print(matrix_3x3)

# Task 3: 
identity_matrix = np.eye(3)
print("\n3x3 identity matrix:")
print(identity_matrix)

# Task 4: 
array_3x3x3 = np.random.random((3, 3, 3))
print("\n3x3x3 array with random values:")
print(array_3x3x3)

# Task 5: 
array_10x10 = np.random.random((10, 10))
min_value = array_10x10.min()
max_value = array_10x10.max()
print("\n10x10 array with random values:")
print(array_10x10)
print(f"Minimum value: {min_value}, Maximum value: {max_value}")

# Task 6: 
random_vector = np.random.random(30)
mean_value = random_vector.mean()
print("\nRandom vector of size 30:")
print(random_vector)
print(f"Mean value: {mean_value}")

# Task 7: 
random_matrix_5x5 = np.random.random((5, 5))
normalized_matrix = (random_matrix_5x5 - random_matrix_5x5.mean()) / random_matrix_5x5.std()
print("\nNormalized 5x5 random matrix:")
print(normalized_matrix)

# Task 8: 
matrix_5x3 = np.random.random((5, 3))
matrix_3x2 = np.random.random((3, 2))
matrix_product = np.dot(matrix_5x3, matrix_3x2)
print("\nProduct of a 5x3 matrix and a 3x2 matrix:")
print(matrix_product)

# Task 9: 
matrix1_3x3 = np.random.random((3, 3))
matrix2_3x3 = np.random.random((3, 3))
dot_product = np.dot(matrix1_3x3, matrix2_3x3)
print("\nDot product of two 3x3 matrices:")
print(dot_product)

# Task 10: 
matrix_4x4 = np.random.random((4, 4))
transpose_matrix = matrix_4x4.T
print("\nTranspose of a 4x4 matrix:")
print(transpose_matrix)

# Task 11: 
matrix_3x3_det = np.random.random((3, 3))
determinant = np.linalg.det(matrix_3x3_det)
print("\nDeterminant of a 3x3 matrix:")
print(determinant)

# Task 12:
matrix_A = np.random.random((3, 4))
matrix_B = np.random.random((4, 3))
matrix_product_AB = np.dot(matrix_A, matrix_B)
print("\nMatrix product of A (3x4) and B (4x3):")
print(matrix_product_AB)

# Task 13: 
matrix_3x3_vec = np.random.random((3, 3))
vector_3 = np.random.random(3)
matrix_vector_product = np.dot(matrix_3x3_vec, vector_3)
print("\nMatrix-vector product of a 3x3 matrix and a 3-element vector:")
print(matrix_vector_product)

# Task 14: 
A = np.random.random((3, 3))
b = np.random.random(3)
x = np.linalg.solve(A, b)
print("\nSolution to the linear system (Ax = b):")
print(x)

# Task 15:
matrix_5x5 = np.random.random((5, 5))
row_sums = matrix_5x5.sum(axis=1)
column_sums = matrix_5x5.sum(axis=0)
print("\nRow-wise sums of a 5x5 matrix:")
print(row_sums)
print("Column-wise sums of a 5x5 matrix:")
print(column_sums)