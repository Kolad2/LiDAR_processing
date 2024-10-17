import cv2
import numpy as np
import matplotlib.pyplot as plt
from rockedgesdetectors import (
	ModelPiDiNet,
	ModelRCF,
	Cropper)


models = {
	"pidinet_5": {
		"model": ModelPiDiNet,
		"checkpoint_path": "../models/pidinetmodels/table5_pidinet.pth"
	},
	"pidinet_7": {
		"model": ModelPiDiNet,
		"checkpoint_path": "../models/pidinetmodels/table7_pidinet.pth"
	},
	"rcf": {
		"model": ModelRCF,
		"checkpoint_path": "../models/RCFcheckpoint_epoch12.pth"
	},
}


def get_model(name):
	return models[name]["model"](models[name]["checkpoint_path"])


model_name = "pidinet_7"
image_load_path = f"..//images_test//IMGP3859_cut.png"
image_save_path = f"..//images_test//IMGP3859_cut_edges.png"

# get edges from model
model = Cropper(get_model(model_name))
image = cv2.imread(image_load_path)
result = model(image)

# save edges image
image = (result/np.max(result)*255).astype(np.uint8)
image = cv2.merge((image, image, image))
cv2.imwrite(image_save_path, image)

fig = plt.figure(figsize=(14, 9))
axs = [fig.add_subplot(1, 1, 1)]
axs[0].imshow(image)
plt.show()

