import mimetypes

file_path = "image.jpg"
mime_type, encoding = mimetypes.guess_type(file_path)

print(f"MIME type: {mime_type}")
print(f"Encoding: {encoding}")
