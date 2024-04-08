import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Picture 1.png')


dst = cv2.fastNlMeansDenoisingColored(img,None,11,6,7,21)
row, col =1,2

fig, axs = plt.subplots(row, col, figsize=(15,10))
fig.tight_layout()
axs[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axs[0].set_title("Noisy Image")
axs[1].imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
axs[1].set_title("Denoise Image")
plt.show()