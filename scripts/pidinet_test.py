import os
import argparse
import time
import cv2

import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
import torch.backends.cudnn as cudnn
import torchvision.transforms as transforms

import matplotlib.pyplot as plt

from rockedgesdetectors import pidinet
from rockedgesdetectors.pidinet.pidinet import PiDiNet
from rockedgesdetectors.pidinet.utils import load_checkpoint
from rockedgesdetectors.pidinet.config import config_model
from rockedgesdetectors.pidinet.convert_pidinet import convert_pidinet


pdcs = config_model('carv4')
model = PiDiNet(60, pdcs, dil=24, sa=True)
model = torch.nn.DataParallel(model).cuda()

checkpoint_path = "../models/pidinetmodels/table7_pidinet.pth"
#checkpoint_path = "../models/pidinetmodels/table5_pidinet.pth"
#checkpoint_path = "../models/pidinetmodels/table5_baseline.pth"
checkpoint = torch.load(checkpoint_path, map_location='cpu')

#pidinet_state_dict = convert_pidinet(checkpoint['state_dict'], 'carv4')
#model.load_state_dict(pidinet_state_dict, strict=False)

model.load_state_dict(checkpoint['state_dict'])

normalize = transforms.Normalize(
    mean=[0.485, 0.456, 0.406],
    std=[0.229, 0.224, 0.225]
)

transform = transforms.Compose(
    [transforms.ToTensor(), normalize]
)

image = cv2.imread(f"..//images//test.png")


image = transform(image).unsqueeze(0).cuda()

#model.eval()
results = model(image)
result = torch.squeeze(results[-1]).detach().cpu().numpy()


fig = plt.figure(figsize=(7, 9))
axs = [fig.add_subplot(1, 1, 1)]
axs[0].imshow(result)
plt.show()


