import pytesseract
from PIL import Image
import json

# Load the image
image_path = '/home/arman/arman/github/exam_project/image.jpg'
img = Image.open(image_path)

# Use Tesseract to do OCR on the image
extracted_text = pytesseract.image_to_string(img, lang='ben+eng')

# Process the extracted text (this will depend on your specific format)
# For example, let's assume we want to extract lines and create a JSON object
lines = extracted_text.split('\n')
data = {
    "text_lines": [line for line in lines if line.strip() != ""]
}

# Convert to JSON
json_output = json.dumps(data, indent=4)

# Save to a JSON file
with open('output.json', 'w') as json_file:
    json_file.write(json_output)

print("JSON file created successfully.")