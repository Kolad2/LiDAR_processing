import cv2
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from pygradskeleton import grayscale_skeletonize

root_path = Path("D:/1.ToSaver/profileimages/photo_database")
edges_weighted_path = root_path / "edges_weighted" / "IMGP3353-3355.png"
edges_thin_path = root_path / "edges_thin" / edges_weighted_path.name


image = cv2.imread(str(edges_weighted_path))
image_thin = grayscale_skeletonize(image, h=75).astype(np.uint8)
_, image_thin = cv2.threshold(image_thin, 75, 255, cv2.THRESH_BINARY)

cv2.imwrite(str(edges_thin_path), image_thin)

fig = plt.figure(figsize=(14, 9))
axs = [fig.add_subplot(1, 1, 1)]
axs[0].imshow(image_thin)
plt.show()
