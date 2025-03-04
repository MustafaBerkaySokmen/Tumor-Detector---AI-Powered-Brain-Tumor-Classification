# -*- coding: cp1254 -*-

import os
import shutil
import pandas as pd
import numpy as np
from PIL import Image

# Set the paths to the data files
data_dirname = r"C:\Users\musta\source\repos\Tümör bulucu"
image_filename = "brainimage.csv"
label_filename = "brain.csv"

# Create directories for train and test data
train_dirname = "train"
train_dir = os.path.join(data_dirname, train_dirname)
os.makedirs(train_dir, exist_ok=True)

test_dirname = "test"
test_dir = os.path.join(data_dirname, test_dirname)
os.makedirs(test_dir, exist_ok=True)

# Create directories for the two classes of data
train_yes_dir = os.path.join(train_dir, "yes")
os.makedirs(train_yes_dir, exist_ok=True)

train_no_dir = os.path.join(train_dir, "no")
os.makedirs(train_no_dir, exist_ok=True)

test_yes_dir = os.path.join(test_dir, "yes")
os.makedirs(test_yes_dir, exist_ok=True)

test_no_dir = os.path.join(test_dir, "no")
os.makedirs(test_no_dir, exist_ok=True)

# Load the labels into a pandas DataFrame
labels = pd.read_csv(os.path.join(data_dirname, label_filename))

# Extract the images and copy them to the appropriate directories
for index, row in labels.iterrows():
    filename = row["Image"]
    has_tumor = row["Class"]

    # Open the image using PIL
    img = Image.open(os.path.join(data_dirname, "beyinlabeyin", filename))

    # Convert the image to a grayscale array
    img_arr = np.array(img.convert("L"))

    # Reshape the array to have 3 dimensions
    img_arr_reshaped = img_arr.reshape((img_arr.shape[0], img_arr.shape[1], 1))

    # Copy the image to the appropriate train or test directory
    if "train" in filename:
        if has_tumor == 1:
            np.save(os.path.join(train_yes_dir, filename), img_arr_reshaped)
        else:
            np.save(os.path.join(train_no_dir, filename), img_arr_reshaped)
    else:
        if has_tumor == 1:
            np.save(os.path.join(test_yes_dir, filename), img_arr_reshaped)
        else:
            np.save(os.path.join(test_no_dir, filename), img_arr_reshaped)
