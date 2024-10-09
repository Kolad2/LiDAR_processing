import cv2
import numpy as np
import matplotlib.pyplot as plt
from rockedgesdetectors import ModelGPU, Cropper


big_frame = cv2.imread("image.png")
model = ModelGPU("../models/RCFcheckpoint_epoch12.pth")
#edges = model.get_model_edges(big_frame)
edges = Cropper(model, big_frame).get_cropped_edges(512, 512, 64, 64)


fig = plt.figure(figsize=(14, 9))
axs = [fig.add_subplot(1, 1, 1)]
axs[0].imshow(edges)
plt.show()



# #
# cv2.imwrite("image_edges.png", edges)
# #
# cv2.namedWindow("wnd", cv2.WINDOW_NORMAL)
# cv2.resizeWindow('wnd', 800, 600)
# cv2.imshow("wnd", big_frame)
# cv2.waitKey(0)
# #
# cv2.namedWindow("wnd", cv2.WINDOW_NORMAL)
# cv2.resizeWindow('wnd', 800, 600)
# cv2.imshow("wnd", edges)
# cv2.waitKey(0)


