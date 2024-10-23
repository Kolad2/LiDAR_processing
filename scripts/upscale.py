import torch
import cv2
from pyrockupscale import RealESRGAN

scale = 4

# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model_path = f"../models/RealESRGAN_x{scale}.pth"
model = RealESRGAN(scale=scale, model_path=model_path, device=torch.device('cpu'))

#file_name = "../images/image.png"
file_name = "../images_test/IMGP3874_cut.png"
image = cv2.cvtColor(cv2.imread(file_name), cv2.COLOR_BGR2RGB)

print("predict start")
sr_image = model.predict(
    image,
    batch_size=4,
    patches_size=192,
    padding=24,
    pad_size=15
)

sr_image.save(f"image_up{scale}.png")


