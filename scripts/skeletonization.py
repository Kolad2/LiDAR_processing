import cv2
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from pygradskeleton import grayscale_skeletonize


edges_weighted_path = Path(f"../images/cut_3_2_edges.png")
image_edges_thin = Path(f"../images/cut_3_2_edges_thin.png")
image = cv2.imread(str(edges_weighted_path))

thin_image = grayscale_skeletonize(image, h=50).astype(np.uint8)
_, thin_image = cv2.threshold(thin_image, 150, 255, cv2.THRESH_BINARY)
print(np.unique(thin_image))

cv2.imwrite(str(image_edges_thin), thin_image)

fig = plt.figure(figsize=(14, 9))
axs = [fig.add_subplot(1, 1, 1)]
axs[0].imshow(thin_image)
plt.show()
