import cv2
from pathlib import Path
from orthostitcher import CV2VideoStitcher

#video_path = Path("../renders/output.mp4")
folder_path = Path("D:/1.ToSaver/profileimages/1/raw_images")

stitcher = CV2VideoStitcher(path_to_folder=str(folder_path))
frame = stitcher.stitch()

cv2.imwrite("../images/image.png", frame)

