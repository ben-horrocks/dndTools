from PIL import Image
from pytesseract import image_to_string
image = Image.open('./20201220_105057.jpg').rotate(-90)
print(image_to_string(image))
image.show()
