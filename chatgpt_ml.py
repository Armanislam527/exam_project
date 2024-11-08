import cv2
import pytesseract
from PIL import Image

# Load the image
image = cv2.imread('/home/arman/arman/github/exam_project/image.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# Apply Gaussian Blur to remove noise
blurred = cv2.GaussianBlur(thresh, (5, 5), 0)

# Save preprocessed image (optional, for checking)
cv2.imwrite("/path/to/preprocessed_image.jpg", blurred)

# Perform OCR
text = pytesseract.image_to_string(blurred, lang="ben+eng")

print(text)
