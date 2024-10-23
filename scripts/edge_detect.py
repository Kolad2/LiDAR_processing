import cv2
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
image_load_path_0 = f"../images_test/IMGP3874_cut.png"
image_load_path = f"../images_test/IMGP3874_cut_up4.png"

image_save_path = f"../images_test/IMGP3874_cut_edges.png"
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


# th_b, _ = cv2.threshold(b, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# th_r, _ = cv2.threshold(r, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# th_g, _ = cv2.threshold(g, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# th_b = 125
# th_r = 125
# th_g = 125
# b[b > th_b] = th_b
# r[r > th_r] = th_r
# g[g > th_g] = th_g

image = cv2.merge((r, g, b))
image_b = cv2.merge((b, b, b))
image_r = cv2.merge((r, r, r))
image_g = cv2.merge((g, g, g))

#_, image_b = cv2.threshold(image_b, threshold_value, 255, cv2.THRESH_BINARY)

# result_b = model(image_b)
# result_r = model(image_r)
# result_g = model(image_g)
result = model(image)
#
# # Создаем объект CLAHE
#
#
# result = np.maximum.reduce((result_b, result_r, result_g))

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

