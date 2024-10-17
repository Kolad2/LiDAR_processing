import cv2
import matplotlib.pyplot as plt
from pygradskeleton import grayscale_skeletonize


image = cv2.imread(f"..//images_test//IMGP3859_cut_edges.png")
thin_image = grayscale_skeletonize(image, h=150)


fig = plt.figure(figsize=(14, 9))
axs = [fig.add_subplot(1, 1, 1)]
axs[0].imshow(thin_image)
plt.show()
