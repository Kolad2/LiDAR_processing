import cv2
from pathlib import Path
from orthostitcher import CV2VideoStitcher


from orthostitcher.datasets import ImagesDataset

from orthostitcher.ortho_stitcher import stitch_dataset

dataset = ImagesDataset()
root_path = Path("D:/1.ToSaver/profileimages/photo_database")
dataset.add_image(root_path / "IMGP3353.png")
dataset.add_image(root_path / "IMGP3354.png")
dataset.add_image(root_path / "IMGP3355.png")
image = stitch_dataset(dataset)
print(image)
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
cv2.imwrite("image.png", image)


# video_path = Path("../renders/output.mp4")
# folder_path = Path("D:/1.ToSaver/profileimages/1/raw_images")
#
# stitcher = CV2VideoStitcher(path_to_folder=str(folder_path))
# frame = stitcher.stitch()
#
# cv2.imwrite("../images/image.png", frame)

