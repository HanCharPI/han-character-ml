import numpy as np
from numpy import ndarray
import skimage.transform
import sys

sys.path.insert(0, "")
from util import image_converter
from label import kanji_label

def process(img_base64: str):
  image = image_converter.base64_to_Image(img_base64.encode('utf-8'))
  image = image_converter.add_white_bg(image)
  image = image_converter.convert_grayscale(image)

  image_np = np.array(image)
  image_np = image_np/255.0
  image_np = skimage.transform.resize(image_np, (48, 48, 1))
  return image_np.reshape((1, 48, 48, 1))

def get_characters(indexes: list):
  kanjis = [kanji_label.labels[index] for index in indexes]
  return kanjis

def get_top(nparray: ndarray, n: int):
  predict_proba = nparray[0]
  sorted_list = np.argsort(predict_proba)[::-1]
  return sorted_list[:n]

