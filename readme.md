🚗 License Plate Recognition (LPR) System
This project implements a basic License Plate Recognition (LPR) system using Python, OpenCV, and Tesseract OCR. It's designed to detect license plates in images, extract the plate region, and then perform Optical Character Recognition (OCR) to read the alphanumeric characters.

✨ Features
Image Loading: Loads a specified image file.

Image Preprocessing: Converts images to grayscale, applies noise reduction (bilateral filter), and performs edge detection (Canny).

Contour Detection: Identifies potential license plate regions using contour analysis.

Shape and Aspect Ratio Filtering: Filters contours based on their shape (quadrilateral) and aspect ratio to accurately pinpoint license plates.

Text Extraction (OCR): Utilizes Google's Tesseract OCR engine to convert the detected license plate image into readable text.

Visual Feedback: Displays the original image with the detected license plate highlighted and the extracted binarized plate image.

Error Handling: Provides informative messages for common issues like image not found or Tesseract not installed.

🛠️ Prerequisites
Before you run this script, ensure you have the following installed on your system:

Python 3.x:

Download from python.org.

OpenCV (Open Source Computer Vision Library):

Install via pip:

pip install opencv-python

Pytesseract:

Python wrapper for Tesseract OCR.

Install via pip:

pip install pytesseract

Tesseract OCR Engine:

This is crucial! Pytesseract is just a wrapper; you need the actual Tesseract OCR executable.

For Windows:

Download the installer from Tesseract at UB Mannheim.

During installation, ensure you select the option to "Add Tesseract to your system PATH" or note down the installation directory (e.g., C:\Program Files\Tesseract-OCR\).

For Linux/macOS:

Refer to the official Tesseract documentation for installation instructions: Tesseract Installation.

Typically installed via package managers (e.g., sudo apt install tesseract-ocr on Debian/Ubuntu, brew install tesseract on macOS).

🚀 Installation and Setup
Clone or Download the Repository:

git clone <repository_url> # If it's in a Git repository
cd "License Plate Recognition System"

Or simply download main.py and car.jpg into a folder.

Install Python Dependencies:

pip install opencv-python pytesseract

Place Your Image:

Ensure your input image (e.g., car.jpg) is located in the same directory as main.py, or update the image_path variable in main.py to point to its correct location.

Configure Tesseract Path (Windows Specific):

Open main.py in a text editor.

Locate the line:

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

Verify this path. If you installed Tesseract to a different location (e.g., C:\Program Files (x86)\Tesseract-OCR\tesseract.exe or a custom directory), update this line accordingly. For Linux/macOS, this line might not be strictly necessary if Tesseract is in your system's PATH.

🏃 Usage
To run the License Plate Recognition system, simply execute the main.py script from your terminal:

python main.py

The script will:

Load the car.jpg image.

Process it to detect a license plate.

Print the detected license plate text to the console.

Display two OpenCV windows:

"Detected License Plate on Image": Shows the original image with a green bounding box around the detected plate and the extracted text.

"Extracted Binarized License Plate": Shows the processed, binarized image of just the license plate region.

Press any key in either OpenCV window to close them and exit the script.

⚙️ Configuration
You can adjust several parameters in main.py to fine-tune the detection and OCR process:

image_path: Change this to the path of the image you want to process.

pytesseract.pytesseract.tesseract_cmd: Crucial for Windows. Set this to the absolute path of your tesseract.exe executable.

MIN_ASPECT_RATIO and MAX_ASPECT_RATIO: These define the acceptable width-to-height ratio for a potential license plate. Adjust these if your target plates have different proportions.

MIN_PLATE_AREA: The minimum pixel area a contour must have to be considered a license plate. Useful for filtering out small noise.

cv2.bilateralFilter parameters: 11, 17, 17 control the diameter of the pixel neighborhood, color sigma, and space sigma, respectively.

cv2.Canny parameters: 170, 200 are the lower and upper thresholds for edge detection.

cv2.dilate kernel size: (3,3) can be adjusted to (5,5) or (2,2) depending on how much you need to connect broken edges.

pytesseract.image_to_string config: --psm 8 (Page Segmentation Mode 8: Treat the image as a single word) and --oem 3 (OCR Engine Mode 3: Default, LSTM + Legacy engine). You can experiment with other PSM modes (e.g., --psm 6 for a single uniform block of text) if results are not optimal.

🐛 Troubleshooting
⚠️ Error: Could not load image... check file path/integrity:

Cause: The script cannot find or open the image file.

Solution:

Verify image_path: Ensure the path in main.py is absolutely correct and matches the file's location and name (including extension).

Special Characters in Path: Avoid emojis or unusual characters in folder names in the path. Rename folders if necessary (e.g., 🚗 License Plate Recognition System to License Plate Recognition System).

File Existence: Confirm the car.jpg file actually exists at the specified location.

Permissions: Ensure your user account has read access to the image file and its parent directories.

❌ Error: Tesseract is not installed or not found in your PATH.:

Cause: The Tesseract OCR engine is either not installed or Pytesseract cannot find its executable.

Solution:

Install Tesseract: Follow the installation instructions in the Prerequisites section.

Verify tesseract_cmd Path: If Tesseract is installed, ensure the pytesseract.pytesseract.tesseract_cmd variable in main.py points to the exact location of your tesseract.exe file.

Add to PATH (Windows): During Tesseract installation, ensure you select the option to add it to your system's PATH. If not, you might need to add it manually or always specify the full path in the script.

Incorrect OCR Results:

Cause: Image quality, lighting, angle, or complex fonts can affect OCR accuracy.

Solution:

Improve Image Quality: Use clearer, higher-resolution images.

Adjust Preprocessing: Experiment with cv2.bilateralFilter, cv2.Canny thresholds, and cv2.dilate kernel size.

Binarization: The current script uses Otsu's binarization. You might try inverting the colors (cv2.bitwise_not(binarized_plate)) if your plates have light text on a dark background.

Tesseract PSM/OEM: Experiment with different --psm (Page Segmentation Mode) and --oem (OCR Engine Mode) configurations in the image_to_string call.

🤝 Contributing
Feel free to fork this repository, open issues, or submit pull requests to improve the system. Suggestions for better detection algorithms, OCR accuracy, or new features are welcome!

📄 License
This project is open-source and available under the MIT License.