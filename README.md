# Tumor Detector - AI-Powered Brain Tumor Classification

## Overview

This project is an **AI-based medical image classification system** that detects the presence of **brain tumors** in MRI scans. It uses **image processing techniques** to clean, preprocess, and categorize images, preparing them for further use in **deep learning-based tumor detection models**.

## Features

- **Loads and Processes MRI Brain Scans** from `image_labels.csv`.
- **Grayscale Conversion & Resizing** for optimized model input.
- **Automated Train-Test Split**, organizing images into structured datasets.
- **NumPy Array Storage** for efficient machine learning training.
- **Supports Deep Learning Integration** for further model development.

## Dataset

The project uses a dataset of **brain MRI scans**, categorized into:

- `` → Brain scans containing tumors.
- `` → Healthy brain scans without tumors.

These classifications are stored in `image_labels.csv`.

## Installation

### **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/Tumor-Detector.git
cd Tumor-Detector
```

### **2. Set Up a Virtual Environment (Optional, but Recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate    # On Windows
```

### **3. Install Dependencies**

```bash
pip install numpy pandas pillow opencv-python
```

## Running the Script

To preprocess and categorize MRI scans:

```bash
python tumor_detector.py
```

## How It Works

### **📌 Step 1: Load Image Data from **``

The script reads `image_labels.csv`, which contains image filenames and tumor presence labels (`1 = Tumor, 0 = No Tumor`).

### **📌 Step 2: Preprocess Images**

Each image undergoes:

- **Grayscale conversion** → Removes color information for better contrast.
- **Resizing** → Standardizes dimensions for deep learning models.
- **Normalization** → Scales pixel values to [0,1] range.

### **📌 Step 3: Organize Data into Folders**

The images are automatically sorted into:

```
📂 dataset/
 ├── 📂 train/
 │   ├── 📂 yes/  # Tumor images for training
 │   ├── 📂 no/   # Non-tumor images for training
 ├── 📂 test/
 │   ├── 📂 yes/  # Tumor images for testing
 │   ├── 📂 no/   # Non-tumor images for testing
```

### **📌 Step 4: Save Preprocessed Data**

The processed images are converted into NumPy arrays (`.npy` format) and stored for future model training.

## Example Output

```
Loading dataset...
Processing image: scan1.jpg (Tumor detected ✅)
Processing image: scan2.jpg (No tumor ❌)
Processing image: scan3.jpg (Tumor detected ✅)
...
Saving preprocessed images to dataset/train/ and dataset/test/
Dataset processing complete! Ready for training.
```

## Next Steps

1. **Train a Deep Learning Model** using TensorFlow/Keras to classify brain tumors.
2. **Expand Dataset** by adding more MRI scans.
3. **Optimize Preprocessing** for higher accuracy in AI models.

## License

This project is licensed under the **MIT License**.

## Contributions

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`feature-new-feature`).
3. Commit and push your changes.
4. Open a pull request.

## Contact

For any questions or support, please open an issue on GitHub.

