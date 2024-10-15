import os
from pathlib import Path
import cv2
import numpy as np
import matplotlib.pyplot as plt
from pyrocksegmentation import Segmentator, Extractor
from rockedgesdetectors import ModelRCF, Cropper


def get_image_path(image_folder, image_name):
	image_path = image_folder / image_name
	for suffix in [".tif", ".tiff", ".png", ".jpg"]:
		if image_path.with_suffix(suffix).exists():
			return image_path.with_suffix(suffix)
	return None


def get_edges_weighted(scale=1, image_folder=Path("."), edges_folder=Path("."), image_name="image"):
	if scale == 1:
		suffix = ""
	else:
		suffix = f"_up{scale}"

	edges_path = (edges_folder / image_name).with_suffix(suffix + ".npy")
	print(image_folder)
	try:
		edges_weighted = np.load(str(edges_path))
		return edges_weighted
	except:
		print("Не найденны веса, попытка генерации")
		model = ModelRCF("../models/RCFcheckpoint_epoch12.pth")
		try:
			image_path = get_image_path(image_folder=image_folder, image_name=image_name)
			image = cv2.imread(str(image_path))
		except:
			return None
		edges_weighted = Cropper(model, image).get_cropped_edges(512, 512, 64, 64)
		np.save(edges_path, edges_weighted)
		return edges_weighted



image_folder = Path("../images/")
edges_folder = Path("../edges")
#image_name = "IMGP3859"
#image_name = "IMGP3874"
image_name = "IMGP3898"
image_path = image_folder / image_name

image = cv2.imread(get_image_path(image_folder=image_folder, image_name=image_name))
height, width, channels = image.shape

edges_weighted = {}
for i in [1]:
	_edges_weighted = get_edges_weighted(
		image_folder=image_folder,
		edges_folder=edges_folder,
		image_name=image_name,
		scale=i)
	if _edges_weighted is not None:
		_edges_weighted = cv2.resize(_edges_weighted, (width, height))
		edges_weighted[f"up{i}"] = _edges_weighted
	else:
		print(f"не найден {i}")


n = len(edges_weighted)

segments = {}
bg = {}
for i in range(1, n+1):
	print(i)
	segmentator = Segmentator(image=image, edges_weighted=edges_weighted[f"up{i}"])
	segmentator.run()
	_bg = 255 - segmentator.background
	_bg = cv2.merge((_bg, _bg, _bg, 255 - _bg))
	bg[f"up{i}"] = _bg
	segments[f"up{i}"] = segmentator.get_segment_image()



# fig = plt.figure(figsize=(7, 9))
# axs = [fig.add_subplot(n+1, 1, i+1) for i in range(n+1)]
# axs[0].imshow(image)
# axs[1].imshow(edges_weighted[f"up1"])
# fig.savefig("edges_weighted.png", dpi=500)
# plt.show()
#
#
# fig = plt.figure(figsize=(7, 9))
# axs = [fig.add_subplot(n+1, 1, i+1) for i in range(n+1)]
# axs[0].imshow(image)
# axs[1].imshow(image)
# axs[1].imshow(bg["up1"])
# fig.savefig("edges.png", dpi=500)
# plt.show()


fig = plt.figure(figsize=(7, 9))
axs = [fig.add_subplot(n+1, 1, i+1) for i in range(n+1)]
axs[0].imshow(image)
axs[1].imshow(image)
axs[1].imshow(segments["up1"], alpha=0.5)
fig.savefig(image_name + "_edges_segments.png", dpi=1000)
plt.show()


