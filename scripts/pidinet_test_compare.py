import cv2
import matplotlib.pyplot as plt
from rockedgesdetectors import ModelPiDiNet
from rockedgesdetectors import ModelRCF, Cropper



image = cv2.imread(f"..//images//test.png")

checkpoint_path_7 = "../models/pidinetmodels/table7_pidinet.pth"
checkpoint_path_5 = "../models/pidinetmodels/table5_pidinet.pth"


model = ModelPiDiNet(checkpoint_path_7)
result_pidinet_1 = model(image)

model = ModelPiDiNet(checkpoint_path_5)
result_pidinet_2 = model(image)


checkpoint_path_rcf = "../models/RCFcheckpoint_epoch12.pth"

model_rcf = ModelRCF(checkpoint_path_rcf)
cropper = Cropper(model_rcf, image)
result_rcf = cropper(image)


fig = plt.figure(figsize=(7, 9))
axs = [fig.add_subplot(3, 2, 1),
       fig.add_subplot(3, 2, 2),
       fig.add_subplot(3, 2, 4),
       fig.add_subplot(3, 2, 6)]

axs[0].imshow(image)
axs[0].set_title("Начальное изображение")

axs[1].imshow(result_rcf)
axs[1].set_title("rcf model")

axs[2].imshow(result_pidinet_1)
axs[2].set_title("pidinet model 5")

axs[3].imshow(result_pidinet_2)
axs[3].set_title("pidinet model 7")

fig.savefig("edges_compare_models.png", dpi=500)
plt.show()


