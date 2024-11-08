import pytesseract
from PIL import Image

# Set the path for tesseract executable if it's not in your PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load your image file
image = Image.open('/home/arman/arman/github/exam_project/image.jpg')

# Specify both Bengali and English for OCR
text = pytesseract.image_to_string(image, lang='ben+eng')

print(text)
