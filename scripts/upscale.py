import torch
from PIL import Image
from pyrockupscale import RealESRGAN

scale = 4

# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
device = torch.device('cpu')
#device = torch.device('cuda')
model = RealESRGAN(device, scale=scale)
model.load_weights(f"../models/RealESRGAN_x{scale}.pth", download=False)

file_name = "image.png"

image = Image.open(file_name).convert('RGB')

print("predict start")
sr_image = model.predict(
    image,
    batch_size=4,
    patches_size=192,
    padding=24,
    pad_size=15
)

sr_image.save(f"image_up{scale}.png")


