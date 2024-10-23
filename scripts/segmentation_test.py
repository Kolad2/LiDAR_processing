import os
from pathlib import Path
import cv2
import numpy as np
import matplotlib.pyplot as plt
from pyrocksegmentation import Segmentator, Extractor

image_path = Path(f"../images_test/IMGP3874_cut.png")
edges_weighted_path = Path(f"../images_test/IMGP3874_cut_edges.png")
thin_edges_path = Path(f'../images_test/IMGP3874_cut_thinedges.png')


image_0 = cv2.imread(str(image_path))
thin_edges = cv2.imread(str(thin_edges_path), 0)
edges_weighted = cv2.imread(str(edges_weighted_path), 0)

segmetator = Segmentator(image_0, edges_weighted=edges_weighted)
# segmetator = Segmentator(image_0, edges=thin_edges)
area_marks = segmetator.run()
image = segmetator.get_segment_image()
# image2 = segmetator.edges
# cv2.imwrite(str(Path('../images_test/IMGP3859_cut_threshholdedges.png')), cv2.merge((image2, image2, image2)))

s = Extractor(area_marks).extruct()
np.save('sampling.npy', s)
exit()

fig = plt.figure(figsize=(6, 6))
axs = [fig.add_subplot(1, 1, 1)]
axs[0].imshow(image_0)
axs[0].imshow(image, alpha=0.3)
fig.savefig("edges.png", dpi=1000)
plt.show()


