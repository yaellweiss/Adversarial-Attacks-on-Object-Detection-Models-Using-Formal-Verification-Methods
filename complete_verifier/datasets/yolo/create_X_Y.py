import numpy as np
import cv2
import os

# Specify the directory containing the .jpg images
directory = './images'

# Get the file names of all the .jpg images in the directory
image_list = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.jpg')]

# Create an empty list to store the image arrays
image_arrays = []

# Loop through the list of image file names
for filename in image_list:
    # Load the image using OpenCV's imread() function and convert it to RGB format
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = cv2.resize(img, (640, 640))
    # Append the RGB image to the list of image arrays
    image_arrays.append(img)

# Convert the list of image arrays to a single 4D array of RGB pixel values using NumPy's stack() function
image_arrays = np.stack(image_arrays, axis=0)

# Save the 4D array of RGB pixel values as a .npy file using NumPy's save() function
np.save('X_yolo.npy', image_arrays)

