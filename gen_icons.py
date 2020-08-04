"""Image convert utils."""
from PIL import Image

img_path: str = input("Path to the image: ")

file_format: str = input("Convert to eg. png, ico, jpeg, etc..: ")

image: Image = Image.open(img_path)

image.save(f"./static/images/favicon.{file_format}")
