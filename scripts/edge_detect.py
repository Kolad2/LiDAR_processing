import cv2
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from rockedgesdetectors import ModelPiDiNet, ModelRCF, Cropper

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
#image_load_path = f"../images_test/IMGP3859_cut.png"

image_load_path_0 = str(Path("D:\\1.ToSaver\\profileimages\\1\\image.png"))
image_load_path = image_load_path_0
image_save_path = str(Path("D:/1.ToSaver/profileimages/1/image_edges.png"))

image_0 = cv2.imread(image_load_path_0)
size_0 = (image_0.shape[1], image_0.shape[0])

image = cv2.imread(image_load_path)
# get edges from model
model = Cropper(get_model(model_name))


b, r, g = cv2.split(image)
clahe = cv2.createCLAHE(clipLimit=10.0, tileGridSize=(25, 25))
b = clahe.apply(b).astype(np.uint8)
r = clahe.apply(r).astype(np.uint8)
g = clahe.apply(g).astype(np.uint8)

image = cv2.merge((r, g, b))
image_b = cv2.merge((b, b, b))
image_r = cv2.merge((r, r, r))
image_g = cv2.merge((g, g, g))

result_b = model(image_b)
result_r = model(image_r)
result_g = model(image_g)
result = model(image)
#
# # Создаем объект CLAHE
#
#
result = np.maximum.reduce((result_b, result_r, result_g, result))

# save edges image
image = (result/np.max(result)*255).astype(np.uint8)
image = cv2.merge((image, image, image))
image = cv2.resize(image, size_0)
cv2.imwrite(image_save_path, image)
#
fig = plt.figure(figsize=(14, 9))
axs = [fig.add_subplot(1, 1, 1)]
axs[0].imshow(image)
plt.show()

