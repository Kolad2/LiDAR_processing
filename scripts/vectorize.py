import cv2
from pathlib import Path
from rocknetmanager.tools import vectorize
from pygradskeleton import grayscale_skeletonize
import numpy as np
import matplotlib.pyplot as plt

root_path = Path("D:/1.ToSaver/profileimages/photo_database")
edges_thin_path = root_path / "edges_thin" / "IMGP3284.png"
shp_folder = root_path / "edges" / edges_thin_path.stem

image_thin = cv2.imread(str(edges_thin_path), 0)
polylines = vectorize(image_thin, shp_folder)

# fig = plt.figure(figsize=(7, 5))
# axs = [fig.add_subplot(1, 2, 1),
#        fig.add_subplot(1, 2, 2)]
# axs[0].imshow(image_thin, cmap='gray')
# axs[1].imshow(image_thin, cmap='gray')
# for polyline in polylines:
#     axs[1].plot(polyline[:, 0], polyline[:, 1])  # , color="blue"
# plt.show()

