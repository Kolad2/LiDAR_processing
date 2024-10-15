import cv2
from orthostitcher import CV2VideoStitcher

video_path = "../renders/output.mp4"


stitcher = CV2VideoStitcher(video_path)
frame = stitcher.stitch()

cv2.imwrite("../images/image.png", frame)

