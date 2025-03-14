import numpy as np
from PIL import Image

# Task 1: Convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

temperatures_f = np.array([32, 68, 100, 212, 77])
vectorized_conversion = np.vectorize(fahrenheit_to_celsius)
temperatures_c = vectorized_conversion(temperatures_f)
print("Temperatures in Celsius:", temperatures_c)

# Task 2: Calculate Power for Each Pair of Numbers
def power(base, exponent):
    return base ** exponent

bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])
vectorized_power = np.vectorize(power)
results = vectorized_power(bases, exponents)
print("Power results:", results)

# Task 3: Solve the System of Equations
A = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])
b = np.array([7, 4, 5])
solution = np.linalg.solve(A, b)
print("Solution to the system of equations:", solution)

# Task 4: Solve the Electrical Circuit Equations
A_circuit = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])
b_circuit = np.array([12, -5, 15])
currents = np.linalg.solve(A_circuit, b_circuit)
print("Currents in the branches (I1, I2, I3):", currents)

# Image Manipulation with NumPy and PIL
def flip_image(image_array):
    flipped_horizontally = np.fliplr(image_array)
    flipped_vertically = np.flipud(image_array)
    return flipped_horizontally, flipped_vertically

def add_noise(image_array):
    noise = np.random.randint(0, 50, image_array.shape, dtype='uint8')
    noisy_image = image_array + noise
    noisy_image = np.clip(noisy_image, 0, 255)
    return noisy_image

def brighten_channels(image_array, value=40):
    brightened_image = image_array + value
    brightened_image = np.clip(brightened_image, 0, 255)
    return brightened_image

def apply_mask(image_array, mask_size=(100, 100)):
    center_x, center_y = image_array.shape[1] // 2, image_array.shape[0] // 2
    start_x, start_y = center_x - mask_size[0] // 2, center_y - mask_size[1] // 2
    end_x, end_y = start_x + mask_size[0], start_y + mask_size[1]
    masked_image = image_array.copy()
    masked_image[start_y:end_y, start_x:end_x] = 0
    return masked_image

# Load the image
image = Image.open('images/birds.jpg')
image_array = np.array(image)

# Perform manipulations
flipped_horizontally, flipped_vertically = flip_image(image_array)
noisy_image = add_noise(image_array)
brightened_image = brighten_channels(image_array)
masked_image = apply_mask(image_array)

# Save the modified images
Image.fromarray(flipped_horizontally).save('flipped_horizontally.jpg')
Image.fromarray(flipped_vertically).save('flipped_vertically.jpg')
Image.fromarray(noisy_image).save('noisy_image.jpg')
Image.fromarray(brightened_image).save('brightened_image.jpg')
Image.fromarray(masked_image).save('masked_image.jpg')