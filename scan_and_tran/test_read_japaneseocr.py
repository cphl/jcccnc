import cv2
import pytesseract
from PIL import Image

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/Tesseract.exe'

# 1. Load the TIFF image
image_path = 'simple.tif'
img = cv2.imread(image_path)

# convert to greyscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Remove Noise (Gaussian Blur)
noise_reduced = cv2.fastNlMeansDenoising(gray, h=10)

# Thresholding (Binary black/white) for OCR accuracy
_, binarized = cv2.threshold(noise_reduced, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Configure Tesseract to use Japanese
# 'jpn' for horizontal, 'jpn_vert' for vertical text
custom_config = r'-l jpn_vert --oem 3 --psm 6'

# Perform OCR
text = pytesseract.image_to_string(img, config=custom_config)

# Print the output
# print(text)

# write to file
with open("output.txt", "w", encoding="utf-8", errors='replace') as f:
	f.write(text)