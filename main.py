import cv2
import pytesseract
import os

# --- Configuration ---
# Update Tesseract path if needed. This path is specific to Windows.
# For Linux/macOS, Tesseract is usually in your PATH, so this line might not be needed.
# If you get a TesseractNotFoundError, ensure Tesseract is installed and its path is correct.
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Use raw string and double backslashes or forward slashes for the image path
# Make sure this image exists at the specified location.
image_path = r"C:/Users/Administrator/OneDrive/Desktop/Python/License Plate Recognition System/car.jpg"

# Define aspect ratio range for typical license plates (width/height)
# These values are approximate and might need adjustment based on your specific images.
# For Indian plates, common ratios are around 1.7 (20x34cm) to 3.09 (11x34cm).
MIN_ASPECT_RATIO = 1.5
MAX_ASPECT_RATIO = 4.0

# Minimum area for a contour to be considered a potential plate
MIN_PLATE_AREA = 400 # This value might need tuning based on image resolution

# --- Main Script ---
def recognize_license_plate(image_path):
    """
    Loads an image, processes it to detect a license plate, and extracts text.

    Args:
        image_path (str): The file path to the input image.
    """
    # Load image
    img = cv2.imread(image_path)

    # Check if image was loaded successfully
    if img is None:
        print(f"⚠️ Error: Could not load image from '{image_path}'. Check the path and file name.")
        return

    # Create a copy of the original image to draw on
    output_img = img.copy()

    # 1. Preprocessing
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply bilateral filter to reduce noise while preserving edges
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    
    # Perform Canny edge detection
    edged = cv2.Canny(gray, 170, 200)

    # Dilate the edges to connect broken parts (helps with contour detection)
    # The kernel size might need adjustment (e.g., (3,3) or (5,5))
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    edged = cv2.dilate(edged, kernel, iterations=1)

    # 2. Contour Detection
    # Find contours in the edged image
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    # Sort contours by area in descending order and take the top 30
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]

    detected_plate_roi = None
    plate_coordinates = None

    # 3. License Plate Identification (Iterate and Filter Contours)
    for contour in contours:
        # Approximate the contour to a polygon
        # The 'epsilon' parameter (10 in your original code) determines the approximation accuracy.
        # A smaller epsilon means a more precise approximation.
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True) # Use a percentage of arc length

        # Check if the approximated contour has 4 vertices (potential rectangle)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(contour) # Get bounding box coordinates

            # Calculate aspect ratio (width / height)
            aspect_ratio = float(w) / h
            
            # Filter by aspect ratio and minimum area
            if MIN_ASPECT_RATIO < aspect_ratio < MAX_ASPECT_RATIO and cv2.contourArea(contour) > MIN_PLATE_AREA:
                # This contour is a strong candidate for a license plate
                detected_plate_roi = gray[y:y + h, x:x + w]
                plate_coordinates = (x, y, w, h)
                break # Found a strong candidate, exit loop

    # 4. Text Extraction (OCR) and Visualization
    if detected_plate_roi is not None:
        # Apply binary thresholding to the extracted plate for better OCR results
        # Otsu's method automatically determines the optimal threshold value
        _, binarized_plate = cv2.threshold(detected_plate_roi, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        # Invert colors if necessary (Tesseract often works better with dark text on light background)
        # You might need to uncomment this based on your image characteristics
        # binarized_plate = cv2.bitwise_not(binarized_plate)

        try:
            # Perform OCR using Pytesseract
            # '--psm 8': Assume a single word (useful for license plates)
            # '--oem 3': Use default Tesseract engine (LSTM + legacy)
            text = pytesseract.image_to_string(binarized_plate, config='--psm 8 --oem 3')
            
            # Clean up the detected text (remove leading/trailing whitespace and common OCR errors)
            clean_text = "".join(filter(str.isalnum, text)).strip().upper()

            print(f"📷 Detected License Plate Text: {clean_text}")

            # Draw the bounding box on the original image
            x, y, w, h = plate_coordinates
            cv2.rectangle(output_img, (x, y), (x + w, y + h), (0, 255, 0), 3) # Green rectangle
            cv2.putText(output_img, clean_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # Display the original image with the bounding box
            cv2.imshow("Detected License Plate on Image", output_img)
            # Display the binarized extracted license plate for inspection
            cv2.imshow("Extracted Binarized License Plate", binarized_plate)
            cv2.waitKey(0) # Wait indefinitely until a key is pressed

        except pytesseract.TesseractNotFoundError:
            print("❌ Error: Tesseract is not installed or not found in your PATH.")
            print("Please install Tesseract OCR engine and ensure its path is correctly set in the script.")
            print("Download from: https://tesseract-ocr.github.io/tessdoc/Installation.html")
        except Exception as e:
            print(f"❌ An error occurred during OCR: {e}")
    else:
        print("⚠️ License plate not detected in the image.")

    cv2.destroyAllWindows() # Close all OpenCV windows

# Call the function to run the LPR process
if __name__ == "__main__":
    recognize_license_plate(image_path)
