import os
from pathlib import Path
import cv2
import numpy as np
import matplotlib.pyplot as plt
from pyrocksegmentation import Segmentator, Extractor
from pyrocksegmentation.basic_segmentator import Segmentator as BSegmentator
from rocknetmanager.tools.shape_load import shape_lines_load

from pyrockstats.distrebutions import lognorm, weibull, paretoexp, rightnorm
from pyrockstats.empirical import ecdf


def get_image_path(image_folder, image_name):
	image_path = image_folder / image_name
	for suffix in [".tif", ".tiff", ".png", ".jpg"]:
		if image_path.with_suffix(suffix).exists():
			return image_path.with_suffix(suffix)
	return None


def get_dists(areas):
	dist = {}
	x, cdf = ecdf(areas)
	theta = lognorm.fit(areas)
	dist["lognorm"] = lognorm(*theta)
	theta = paretoexp.fit(areas)
	dist["paretoexp"] = paretoexp(*theta)
	theta = weibull.fit(areas)
	dist["weibull"] = weibull(*theta)
	theta = rightnorm.fit(areas)
	print(theta)
	dist["rightnorm"] = rightnorm(*theta)
	dist["ecdf"] = {"x": x, "cdf": cdf}
	return dist
#
#
line_width = 3

image_name = "IMGP3859"
root_path = Path("D:/1.ToSaver/profileimages/photo_database_complited")
image_folder = root_path / image_name
image_path = (image_folder / image_name).with_suffix(".png")
lines_edges_folder = image_folder / "traces" / "IMGP3859.shp"
#
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#
lines, bbox = shape_lines_load(lines_edges_folder)

zero_image = np.zeros(image.shape, np.uint8)
image_poly = cv2.polylines(zero_image, lines, False, (255, 255, 255), line_width)
image_poly, _, _ = cv2.split(image_poly)

seg = BSegmentator(edges=image_poly)
seg.run()
areas = Extractor(seg.area_marks).extruct()
image_poly = seg.get_segment_image()

dist = get_dists(areas)


fig = plt.figure(figsize=(9, 4))
axs = [
	fig.add_subplot(1, 3, (1, 2)),
	fig.add_subplot(1, 3, 3)
]

axs[0].imshow(image)
axs[0].imshow(image_poly, alpha=0.5)
x = dist["ecdf"]["x"]
axs[1].plot(x, dist["ecdf"]["cdf"])
axs[1].plot(x, dist["lognorm"].cdf(x), color="blue", label="lognorm")
# axs[1].plot(x, dist["paretoexp"].cdf(x), color="red", label="paretoexp")
# axs[1].plot(x, dist["weibull"].cdf(x), color="green", label="weibull")
axs[1].plot(x, dist["rightnorm"].cdf(x), color="red", label="rightnorm")
#axs[1].plot(x, rightnorm(500, 1000).cdf(x), color="red", label="rightnorm")
axs[1].set_xscale('log')
axs[1].legend(loc='lower right')
plt.tight_layout()
plt.show()


# fig = plt.figure(figsize=(9, 4))
# axs = [
# 	fig.add_subplot(1, 3, (1, 2)),
# 	fig.add_subplot(1, 3, 3)
# ]
# axs[1].plot(x, rightnorm(500, 100).pdf(x), color="red", label="rightnorm")
# axs[1].set_xscale('log')
# plt.show()
