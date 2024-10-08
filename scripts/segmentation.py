import cv2
from pyrocksegmentation import RockImageSegmentator
from rockedgesdetectors import ModelGPU

image = cv2.imread("image.png")

model = ModelGPU("../models/RCFcheckpoint_epoch12.pth")
edges_weighted = model.get_model_edges(image)

segmentator = RockImageSegmentator(image=image, edges_weighted=edges_weighted)
segmentator.run()