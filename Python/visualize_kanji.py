import numpy as np
import matplotlib.pyplot as plt

kanjis = np.load("kanji_train_images.npz")['arr_0'].astype(np.float32)

print("Starting visualization")
plt.figure(figsize=(6,6)).patch.set_facecolor('#ffffff')
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(kanjis[i], cmap=plt.cm.binary)
plt.show()