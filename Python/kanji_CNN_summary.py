from tensorflow import keras
import numpy as np
from keras import backend as K

test_images = np.load("kanji_test_images.npz")['arr_0']
test_labels = np.load("kanji_test_labels.npz")['arr_0']

if K.image_data_format() == "channels_first":
  test_images = test_images.reshape(test_images.shape[0], 1, 48, 48)
  shape = (1, 48, 48)
else:
  test_images = test_images.reshape(test_images.shape[0], 48, 48, 1)
  shape = (48, 48, 1)

model = keras.models.load_model("kanji.h5")

# Get model summary
model.summary()

# Evaluate model accuracy
test_loss, test_acc = model.evaluate(test_images, test_labels)
print("Test Accuracy: ", test_acc)

# Lastest accuracy:
#  - 87% - 0.8693116903305054