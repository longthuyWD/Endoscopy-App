from GUI.ui_GenerateDialog import *
from Function.function import *
from Function.function_dialog import *

import albumentations as A

from models import create_model
import torch
from torchvision import transforms
import os
from models import networks
from PIL import Image
import cv2
import numpy as np 


def showGenerateDialog(self):
    self.dialog = QDialog()
    self.dialog.ui = Ui_GenerateDialog()
    self.dialog.ui.setupUi(self.dialog)
    
    # self.dialog.ui.cyclegan.clicked.connect(lambda: state(self, 'cyclegan'))
    self.dialog.ui.fice.clicked.connect(lambda: state(self, 'fice'))
    self.dialog.ui.lci.clicked.connect(lambda: state(self, 'lci'))
    self.dialog.ui.albumentation.clicked.connect(lambda: state(self, 'albumentation'))
    # self.dialog.ui.vae.clicked.connect(lambda: state(self, 'vae'))

    self.dialog.ui.btnConfirm.clicked.connect(lambda: confirmResize(self))
    self.dialog.ui.btnCancel.clicked.connect(lambda: cancelDialog(self))

    self.dialog.exec_()

def confirmResize(self):
    changeStateClicked(self)
    if self.method == 'lci':
        self.mode = 'lci'
    if self.method == 'fice':
        self.mode = 'fice'
    if self.method == 'albumentation':
        self.mode = 'albumentation'
    self.dialog.close()

def cancelDialog(self):
    self.dialog.close()

def apply_augment(img, tf):
    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgAT = tf(image = image)['image']
    imgATsave = cv2.cvtColor(imgAT, cv2.COLOR_RGB2BGR)
    return imgATsave

def applyMethod(self, image):
    if self.method == 'albumentation':
        changeBrightness(self, image)
    # if self.method == 'vae':
#         self.ui.graphicsView2.hide()
#         self.ui.sourceImage.hide()
#         self.ui.destinationImage.hide()
#         VAE_model(self)
    if self.method == 'lci':
        cycleganMode(self, image, self.mode)
    if self.method == 'fice':
        cycleganMode(self, image, self.mode)


def changeBrightness(self, image):
    inten = [-0.15, 0.15]
    b = 0.15
    c = 0.15
    tf = A.RandomBrightnessContrast((b-0.01, b+0.01), (c-0.01, c+0.01), p=1)
    imgNew = apply_augment(image, tf)
    self.imageDest = imgNew
    showImage(self)
    showImageGenerated(self)

# def VAE_model(self):
#     x = torch.rand(1, 3, 240, 240)
#     encoded = subVAE.encoder(x)
#     mu, logVar = subVAE.fc_mu(encoded), subVAE.fc_var(encoded)
#     std = torch.exp(logVar/2)
#     p = torch.distributions.Normal(torch.zeros_like(mu), torch.ones_like(std))
#     z = p.rsample((1,))
#     meanImg, stdImg = torch.tensor([0.485, 0.456, 0.406]), torch.tensor([0.229, 0.224, 0.225])
#     # SAMPLE IMAGES
#     with torch.no_grad():
#         preds = subVAE.decoder(z.to(subVAE.device)).cpu()
#     for pred in preds:
#         img = pred.permute([1, 2, 0]).mul(stdImg).add(meanImg).numpy()
#         img = np.interp(img, (img.min(), img.max()), (0, 255)).astype(np.uint8)
#         img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
#         m = random.randint(0, 100)
#         # cv2.imwrite(os.path.join(folder, f'{imgName[:-4]}_{m}.jpg'), img)
#         self.image = img
#         showImage(self)

def load_generator(mode):
    load_path = 'weights/wli2{}/latest_net_G.pth'.format(mode)
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = networks.define_G(3, 3, 64, 'resnet_9blocks', use_dropout=False, init_type='normal', init_gain=0.02, norm='instance')
    state_dict = torch.load(load_path, map_location=str(device))
    model.load_state_dict(state_dict)
    return model

def __make_power_2(img, base, method=Image.BICUBIC):
    ow, oh = img.size
    h = int(round(oh / base) * base)
    w = int(round(ow / base) * base)
    if h == oh and w == ow:
        return img
    return img.resize((w, h), method)


def tensor2im(input_image, imtype=np.uint8):
    if not isinstance(input_image, np.ndarray):
        if isinstance(input_image, torch.Tensor): # get the data from a variable
            image_tensor = input_image.data
        else:
            return input_image
        image_numpy = image_tensor[0].cpu().float().numpy() # convert it into a numpy array
        if image_numpy.shape[0] == 1: # grayscale to RGB
            image_numpy = np.tile(image_numpy, (3, 1, 1))
        image_numpy = (np.transpose(image_numpy, (1, 2, 0)) + 1) / 2.0 * 255.0 # post-processing: tranpose and scaling
    else: # if it is a numpy array, do nothing
        image_numpy = input_image
    return image_numpy.astype(imtype)

def cycleganMode(self, image, mode):
    gen = load_generator(mode)
    gen.eval()
    transform = transforms.Compose([transforms.Lambda(lambda img: __make_power_2(img, base=4, method=Image.BICUBIC)), transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    back = transforms.ToPILImage()
    imgInp = Image.fromarray(np.uint8(image)).convert('RGB')
    w, h = imgInp.size
    imgInp = imgInp.resize((int(w/2), int(h/2)))
    imgInp = transform(imgInp).unsqueeze(0)
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    gen=gen.to(device)
    imgInp = imgInp.to(device)
    result=gen(imgInp)

    imgRes=tensor2im(result)
    h, w, d = imgRes.shape
    self.imageDest = cv2.resize(imgRes, dsize=(w*2, h*2))

    showImage(self)
    showImageGenerated(self)

def saveDestImage(self, imageName, saveFol):
    cv2.imwrite(os.path.join(saveFol, imageName), self.imageDest)
    if self.all == False:
        mes(self, None, 'You save file successfully in folder: ' + saveFol)

def generateFolder(self, infoList, saveFol):
    self.all = True
    dialog = QProgressDialog('Tạo ảnh fake trên toàn thư mục', 'Dừng chạy', 0, len(infoList))
    dialog.setWindowTitle('Tạo ảnh fake trên thư mục')
    dialog.setWindowModality(Qt.WindowModal)
    i = 0
    for fileInfo in infoList:
        # if dialog.canceled == True:
        #     break
        absPath = fileInfo.absoluteFilePath()
        absName = os.path.basename(absPath)
        self.image = cv2.imread(absPath)
        dialog.setValue(i)
        dialog.setLabelText(absName)
        i+=1
        applyMethod(self, self.image)
        saveDestImage(self, absName, saveFol)
    mes(self, 'Notification!', 'You save ALL file successfully!')
    self.all = False
