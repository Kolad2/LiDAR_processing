import os
from pathlib import Path
import cv2
import numpy as np
import matplotlib.pyplot as plt
from pyrocksegmentation import Segmentator, Extractor

image_path = Path("..\\images_test\\IMGP3859_cut.png")
edges_weighted_path = Path("..\\images_test\\IMGP3859_cut_edges.png")
thin_edges_path = Path('..\\images_test\\IMGP3859_cut_thinedges.png')

image = cv2.imread(str(image_path))
thin_edges = cv2.imread(str(thin_edges_path), 0)

segmetator = Segmentator(image, edges=thin_edges)
image = segmetator.run()


fig = plt.figure(figsize=(7, 9))
axs = [fig.add_subplot(1, 1, 1)]
axs[0].imshow(image)
# fig.savefig("edges.png", dpi=500)
plt.show()


