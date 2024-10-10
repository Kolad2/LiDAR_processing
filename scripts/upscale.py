import torch
from PIL import Image
from pyrockupscale import RealESRGAN


# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
device = torch.device('cpu')
#device = torch.device('cuda')
model = RealESRGAN(device, scale=4)
model.load_weights('../models/RealESRGAN_x4.pth', download=False)

image = Image.open(f"image.png").convert('RGB')

print("predict start")
sr_image = model.predict(image, batch_size=4, patches_size=192,
                padding=24, pad_size=15)

sr_image.save(f"image_up4.png")