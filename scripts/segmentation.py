import cv2
import numpy as np
from pyrocksegmentation import Segmentator, Extractor
from rockedgesdetectors import ModelGPU

image = cv2.imread("image.png")

# model = ModelGPU("../models/RCFcheckpoint_epoch12.pth")
# edges_weighted = model.get_model_edges(image)
# np.save('edges_weighted.npy', edges_weighted)

edges_weighted = np.load('edges_weighted.npy')

segmentator = Segmentator(image=image, edges_weighted=edges_weighted)
segments = segmentator.run()

extractor = Extractor(segments)
S = extractor.extruct()

sampling = np.array(S)

np.save('sampling.npy', sampling)

print(S)


