from PIL import Image
import PIL.ImageOps
import base64
from io import BytesIO

def base64_to_Image(img_base64: bytes):
  img_decoded = base64.b64decode(img_base64)
  img_file = BytesIO(img_decoded)
  return Image.open(img_file)

def add_white_bg(image: Image):
  img_bg = Image.new("RGB", image.size, color=(255, 255, 255))
  img_bg.paste(image, mask=image.split()[3])
  return img_bg

def convert_grayscale(image: Image):
  img_gray = image.convert('L')
  return PIL.ImageOps.invert(img_gray)