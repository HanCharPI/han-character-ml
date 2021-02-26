import struct, os
from PIL import Image
import numpy as np
from labels.hiragana_label import label

def string_unicode_to_han(unicode):
    han_unicode = '\\u{}'.format(unicode)
    return han_unicode.encode('ascii').decode('unicode-escape')

def file_path_narray(filepath):
    im = Image.open(filepath)
    return im.convert('L')

def read_kanji():
    """
    881 - kanji excluding hiragana characters
    161 - images by writers
    127 - width
    128 - height
    """
    kanji = np.zeros([881, 161, 127, 128], dtype=np.uint8)
    foldername = "../dataset/ETL8G/"
    i = 0
    print("Reading images...")
    for folder in os.scandir(foldername):
        # Decode unicode to han character
        han_char = string_unicode_to_han(folder.name[2:])

        if han_char not in label:
            j = 0
            for file in os.scandir(folder.path):
                if file.name != ".char.txt":
                    # Convert file to Pillow image and then to numpy array
                    iL = file_path_narray(file.path)
                    kanji[i, j] =  np.array(iL)
                    j += 1
            i += 1
    print("Finished reading images")
    # Finish compressing kanji dataset
    print("Compressing images...")
    np.savez_compressed("kanji.npz", kanji)
    print("Finished compressing")

read_kanji()