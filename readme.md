## License Plate Recognition (LPR) System 🚗

 This project implements a basic License Plate Recognition (LPR) system using Python, OpenCV, and Tesseract OCR. It's designed to detect license plates in images, extract the plate region, and then perform Optical Character Recognition (OCR) to read the alphanumeric characters.

## ✨ Features

* **1. Image Loading:** Loads a specified image file.
* **2. Image Preprocessing:** Converts images to grayscale, applies noise reduction (bilateral filter), and performs edge detection (Canny).
* **3. Contour Detection:** Identifies potential license plate regions using contour analysis.
* **4. Shape and Aspect Ratio Filtering:** Filters contours based on their shape (quadrilateral) and aspect ratio to accurately pinpoint license plates.
* **5. Text Extraction (OCR):** Utilizes Google's Tesseract OCR engine to convert the detected license plate image into readable text.
* **6. Visual Feedback:** Displays the original image with the detected license plate highlighted and the extracted binarized plate image.
* **7. Error Handling:** Provides informative messages for common issues like image not found or Tesseract not installed.

## 🛠️ Prerequisites

* **Before you run this script, ensure you have the following installed on your system:**
**Python 3.X**
**Download from "python.org"**
* **OpenCV (Open Source Computer Vision Library):**
### Install via pip:
```bash
pip install opencv-python
```
### Pytesseract:
* **Python wrapper for Tesseract OCR.**
### Install via pip:
```bash
pip install pytesseract
```
### Tesseract OCR Engine:
* **This is crucial! Pytesseract is just a wrapper; you need the actual Tesseract OCR executable.**

### For Windows:

* **Download the installer from Tesseract at UB Mannheim.**
* **During installation, ensure you select the option to "Add Tesseract to your system PATH" or note down the installation directory (e.g., C:\Program Files\Tesseract-OCR).**

### For Linux/macOS:

* **Refer to the official Tesseract documentation for installation instructions: Tesseract Installation.**

## 🚀 Installation and Setup

### Clone or Download the Repository:

```bash
git clone <repository_url>
cd "License Plate Recognition System"
```
### Install Python Dependencies:
```bash
pip install opencv-python pytesseract
```
* **Place Your Image:** Ensure your input image (e.g., car.jpg) is located in the same directory as main.py.

* **Configure Tesseract Path (Windows Specific):**
* **Locate the line:** pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" and verify the path.

## 🏃 Usage

### To run the system, execute:
```bash
python main.py
```
### The script will display:

* **1. "Detected License Plate on Image":** Original image with green bounding box.
* **2. "Extracted Binarized License Plate":** Processed image of the plate.

## ⚙️ Configuration

* **You can adjust several parameters in main.py:**
* **image_path:** Path to your target image.
* **MIN_ASPECT_RATIO and MAX_ASPECT_RATIO:** Acceptable plate proportions.
* **cv2.Canny parameters:** Lower and upper thresholds for edge detection.
* **--psm 8:** Tesseract configuration for single-word recognition.

## 🐛 Troubleshooting

* **⚠️ Error:** Could not load image: Check file path or remove emojis/special characters from folder names.
* **❌ Error:** Tesseract not found: Ensure the engine is installed and the path is correctly set in the script.
* **Incorrect OCR:** Try adjusting binarization or Canny thresholds for clearer character definition.

## 🤝 Contributing

* **Feel free to fork this repository, open issues, or submit pull requests to improve the system.**

## 📄 License

* **This project is open-source and available under the MIT License.**
