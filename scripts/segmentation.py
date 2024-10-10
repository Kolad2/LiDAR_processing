import cv2
import numpy as np
import matplotlib.pyplot as plt
from pyrocksegmentation import Segmentator, Extractor
from rockedgesdetectors import ModelGPU, Cropper


image = cv2.imread("image.png")

# model = ModelGPU("../models/RCFcheckpoint_epoch12.pth")
# #edges_weighted = model.get_model_edges(image)
# edges_weighted = Cropper(model, image).get_cropped_edges(512, 512, 64, 64)
# np.save('edges_weighted.npy', edges_weighted)

edges_weighted = np.load('edges_weighted.npy')

# fig = plt.figure(figsize=(14, 9))
# axs = [fig.add_subplot(1, 1, 1)]
# axs[0].imshow(edges_weighted)
# plt.show()

segmentator = Segmentator(image=image, edges_weighted=edges_weighted)
segments = segmentator.run()
exit()

fig = plt.figure(figsize=(14, 9))
axs = [fig.add_subplot(1, 1, 1)]
axs[0].imshow(segments)
plt.show()

extractor = Extractor(segments)
S = extractor.extruct()

sampling = np.array(S)

np.save('sampling.npy', sampling)

print(S)


