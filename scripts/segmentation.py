import cv2
import numpy as np
import matplotlib.pyplot as plt
from pyrocksegmentation import Segmentator, Extractor
from rockedgesdetectors import ModelGPU, Cropper


image = cv2.imread("image_up4.png")


# model = ModelGPU("../models/RCFcheckpoint_epoch12.pth")
# # #edges_weighted = model.get_model_edges(image)
# edges_weighted = Cropper(model, image).get_cropped_edges(512, 512, 64, 64)
# np.save('edges_weighted_up4.npy', edges_weighted)


edges_weighted_up1 = np.load('edges_weighted.npy')
edges_weighted_up2 = np.load('edges_weighted_up2.npy')
edges_weighted_up4 = np.load('edges_weighted_up4.npy')
edges_weighted_up8 = np.load('edges_weighted_up8.npy')


image = cv2.imread("image.png")
height, width, channels = image.shape
edges_weighted_up2 = cv2.resize(edges_weighted_up2, (width, height))
edges_weighted_up4 = cv2.resize(edges_weighted_up4, (width, height))
edges_weighted_up8 = cv2.resize(edges_weighted_up8, (width, height))

fig = plt.figure(figsize=(14, 9))
axs = [fig.add_subplot(5, 1, 1),
       fig.add_subplot(5, 1, 2),
       fig.add_subplot(5, 1, 3),
       fig.add_subplot(5, 1, 4),
       fig.add_subplot(5, 1, 5)]
axs[0].imshow(image)
axs[1].imshow(edges_weighted_up1)
axs[2].imshow(edges_weighted_up2)
axs[3].imshow(edges_weighted_up4)
axs[4].imshow(edges_weighted_up8)

segmentator = Segmentator(image=image, edges_weighted=edges_weighted_up1)
segments_up1 = segmentator.run()

segmentator = Segmentator(image=image, edges_weighted=edges_weighted_up2)
segments_up2 = segmentator.run()

segmentator = Segmentator(image=image, edges_weighted=edges_weighted_up4)
segments_up4 = segmentator.run()

fig = plt.figure(figsize=(14, 9))
axs = [fig.add_subplot(3, 1, 1),
       fig.add_subplot(3, 1, 2),
       fig.add_subplot(3, 1, 3)]
axs[0].imshow(segments_up1)
axs[1].imshow(segments_up2)
axs[2].imshow(segments_up4)
plt.show()


exit()
extractor = Extractor(segments)
S = extractor.extruct()

sampling = np.array(S)

np.save('sampling.npy', sampling)

print(S)


