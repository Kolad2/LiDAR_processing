import cv2
import matplotlib.pyplot as plt
import numpy as np

from pygradskeleton import grayscale_skeletonize


image = cv2.imread(f"../images_test/IMGP3874_cut_edges.png")
thin_image = grayscale_skeletonize(image, h=50).astype(np.uint8)
_, thin_image = cv2.threshold(thin_image, 150, 255, cv2.THRESH_BINARY)
print(np.unique(thin_image))

cv2.imwrite(f"../images_test/IMGP3874_cut_thinedges.png", thin_image)

fig = plt.figure(figsize=(14, 9))
axs = [fig.add_subplot(1, 1, 1)]
axs[0].imshow(thin_image)
plt.show()
