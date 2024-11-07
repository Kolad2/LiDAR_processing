import cv2
from rocknetmanager.tools import vectorize


image_thin = cv2.imread("../images/cut_3_2_edges_thin.png",0)

vectorize(image_thin)



