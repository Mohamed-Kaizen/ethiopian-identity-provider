"""Utils that create images for PWA."""
from PIL import Image

size_list = [
    (48, 48),
    (72, 72),
    (96, 96),
    (128, 128),
    (144, 144),
    (152, 152),
    (168, 168),
    (192, 192),
    (384, 384),
    (512, 512),
]
img_path = input("Path to the image: ")

image = Image.open(img_path)

for size in size_list:
    size_name = size[0]

    resize_image = image.resize(size)

    resize_image.save(f"./static/images/icon_{size_name}.png")
