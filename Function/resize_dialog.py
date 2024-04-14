import PIL
import tensorflow as tf
# from tensorflow.keras import Model
# from tensorflow.keras.layers import Conv2D, Input, Conv2DTranspose
# from tensorflow.keras.layers import concatenate
from tensorflow.keras.preprocessing.image import array_to_img, img_to_array

from Function.function import *
from Function.function_dialog import *
from GUI.ui_ResizeDialog import *

import os
import numpy as np
import cv2
from PIL import Image
import torch
from torch.utils.data import DataLoader,Dataset
import albumentations
import segmentation_models_pytorch as smp


def showResizeDialog(self):
    self.dialog = QDialog()
    self.dialog.ui = Ui_ResizeDialog()
    self.dialog.ui.setupUi(self.dialog)

    self.resizedWidth = self.dialog.ui.width
    self.resizedHeight = self.dialog.ui.height
    self.state = 'custom'
    
    # self.resizedWidth.setPlaceholderText(str(self.imageWidth))
    # self.resizedHeight.setPlaceholderText(str(self.imageHeight))

    self.dialog.ui.custom.clicked.connect(lambda: state(self, 'custom'))
    self.dialog.ui.aspect.clicked.connect(lambda: state(self, 'aspect'))

    self.resizedWidth.textChanged.connect(lambda: changeStateClicked(self))
    self.dialog.ui.resolution.currentTextChanged.connect(lambda: selectRes(self, self.dialog.ui.resolution))

    self.dialog.ui.btnConfirm.clicked.connect(lambda: confirmResize(self))
    self.dialog.ui.btnCancel.clicked.connect(lambda: cancelDialog(self))

    self.dialog.exec_()


def selectRes(self, cbb):
    if cbb.currentText() == 'Standard': 
        self.resizedWidth.setText('1280')
        self.resizedHeight.setText('960')
    if cbb.currentText() == 'VGA':
        self.resizedWidth.setText('800')
        self.resizedHeight.setText('600')
    if cbb.currentText() == 'HD':
        self.resizedWidth.setText('1366')
        self.resizedHeight.setText('768')
    if cbb.currentText() == 'Full HD':
        self.resizedWidth.setText('1920')
        self.resizedHeight.setText('1080')

def confirmResize(self):
    self.dialog.close()

def cancelDialog(self):
    self.dialog.close()

def resizeImage(self, image):
    try:
        width = toNum(self, self.resizedWidth.text())
        height = toNum(self, self.resizedHeight.text())
        image = cv2.resize(src=image, dsize=(width, height))
        self.image = image
        showImage(self)
        changeSpinBox(self)
    except:
        mes(self, 'Notification!', 'Please choose resolution in \'Config\'')

def resizeFolder(self, infoList, saveFol):
    self.all = True
    dialog = QProgressDialog('Đang đánh giá độ sạch trên toàn thư mục', 'Dừng chạy', 0, len(infoList))
    dialog.setWindowTitle('Đánh giá độ sạch trên thư mục')
    dialog.setWindowModality(Qt.WindowModal)
    i = 0
    for fileInfo in infoList:
        absPath = fileInfo.absoluteFilePath()
        absName = os.path.basename(absPath)
        self.image = cv2.imread(absPath)
        resizeImage(self, self.image)
        dialog.setValue(i)
        dialog.setLabelText(absName)
        i+=1
        saveFile(self, absName, saveFol)
    mes(self, 'Notification!', 'You save ALL file successfully!')
    self.all = False


# def get_model(channel_axis=1, nblocks=8, nlayers=8):
#     def RDBlocks(input, i, nlayers):
#         logits = Conv2D(filters=16, kernel_size=3, padding="same", activation="relu",
#                         use_bias=True, name="conv2d_%d_%d" % (i + 1, 0 + 1))(input)
#         for j in range(1, nlayers):
#             middle = Conv2D(filters=16, kernel_size=3, padding="same", activation="relu",
#                             use_bias=True, name="conv2d_%d_%d" % (i + 1, j + 1))(logits)
#             logits = concatenate([logits, middle], name="concatenate_%d_%d" % (i + 1, j + 1))
#             return logits
#
#     inp = Input(shape=(None, None, channel_axis))
#     x = Conv2D(filters=16, kernel_size=3, strides=1, padding='same', activation='relu', use_bias=True)(inp)
#     G = x
#     for i in range(nblocks):
#         x = RDBlocks(x, i, nlayers)
#         x = concatenate([x, G])
#
#     # bottleneck layer
#     x = Conv2D(filters=256, kernel_size=1, padding='same', activation='relu', use_bias=True)(x)
#     # deconvolution layers
#     x = Conv2DTranspose(256, kernel_size=3, strides=2, padding='same', activation='relu', use_bias=True)(x)
#     # x = layers.Conv2DTranspose(256, kernel_size=3, strides=2, padding='same', activation='relu', use_bias=True)(x)
#     # x = layers.Conv2D(channel_axis*(2**2), kernel_size=3, padding='same', use_bias=True)(x)
#     # x = tf.nn.depth_to_space(x, 2)
#     # reconstruction layer
#     x = Conv2D(filters=channel_axis, kernel_size=3, padding='same', use_bias=True)(x)
#     return Model(inputs=inp, outputs=x)
#
# def get_modelx4(channel_axis=1, nblocks=8, nlayers=8):
#     def RDBlocks(input, i, nlayers):
#         logits = Conv2D(filters=16, kernel_size=3, padding="same", activation="relu",
#                         use_bias=True, name="conv2d_%d_%d" % (i + 1, 0 + 1))(input)
#         for j in range(1, nlayers):
#             middle = Conv2D(filters=16, kernel_size=3, padding="same", activation="relu",
#                             use_bias=True, name="conv2d_%d_%d" % (i + 1, j + 1))(logits)
#             logits = concatenate([logits, middle], name="concatenate_%d_%d" % (i + 1, j + 1))
#             return logits
#
#     inp = Input(shape=(None, None, channel_axis))
#     x = Conv2D(filters=16, kernel_size=3, strides=1, padding='same', activation='relu', use_bias=True)(inp)
#     G = x
#     for i in range(nblocks):
#         x = RDBlocks(x, i, nlayers)
#         x = concatenate([x, G])
#
#     # bottleneck layer
#     x = Conv2D(filters=256, kernel_size=1, padding='same', activation='relu', use_bias=True)(x)
#     # deconvolution layers
#     x = Conv2DTranspose(256, kernel_size=3, strides=2, padding='same', activation='relu', use_bias=True)(x)
#     x = Conv2DTranspose(256, kernel_size=3, strides=2, padding='same', activation='relu', use_bias=True)(x)
#     # x = layers.Conv2D(channel_axis*(2**2), kernel_size=3, padding='same', use_bias=True)(x)
#     # x = tf.nn.depth_to_space(x, 2)
#     # reconstruction layer
#     x = Conv2D(filters=channel_axis, kernel_size=3, padding='same', use_bias=True)(x)
#     return Model(inputs=inp, outputs=x)

# sinh ảnh upscale
def upscale_image(model, img):
    ycbcr = img.convert("YCbCr")
    y, cb, cr = ycbcr.split()
    y = img_to_array(y)
    y = y.astype("float32") / 255.0
    input = np.expand_dims(y, axis=0)
    out = model.predict(input)
    out_img_y = out[0]
    out_img_y *= 255.0
    out_img_y = out_img_y.clip(0, 255)
    out_img_y = out_img_y.reshape((np.shape(out_img_y)[0], np.shape(out_img_y)[1]))
    out_img_y = PIL.Image.fromarray(np.uint8(out_img_y), mode="L")
    out_img_cb = cb.resize(out_img_y.size, PIL.Image.BICUBIC)
    out_img_cr = cr.resize(out_img_y.size, PIL.Image.BICUBIC)
    out_img = PIL.Image.merge("YCbCr", (out_img_y, out_img_cb, out_img_cr)).convert("RGB")
    return out_img

# Thêm code của bạn vào đây
def resizeImage(self, image):  # image phải chuyển về định dạng là numpy array
    with tf.device('/CPU:0'):
        print(str(self.state[0]))
        model = tf.keras.models.load_model(os.getcwd()+'\\ESPCN_modelx%s'%str(self.state[0]))
        pil_image = array_to_img(image)
        self.image = upscale_image(model, pil_image)
        self.image = img_to_array(self.image).astype('uint8')
        showImage(self)
        # Ảnh sinh ra thì gán vào biến 'self.image' và phải có định dạng là numpy array
        ## câu lệnh chuyển từ pil image sang numpy array image
        # opencvImage = cv2.cvtColor(numpy.array(pil_image), cv2.COLOR_RGB2BGR)
        # pass

def resizeImagex4(self, image):  # image phải chuyển về định dạng là numpy array
    with tf.device('/CPU:0'):
        w,h,c = image.shape
        image_d2 = cv2.resize(image, (h//2,w//2), interpolation=cv2.INTER_CUBIC)
        image_d4 = cv2.resize(image, (h//4,w//4), interpolation=cv2.INTER_CUBIC)

        model = tf.keras.models.load_model(os.getcwd() + '\\ESPCN_modelx2')
        # model = tf.keras.models.load_model(os.getcwd()+'\\SRDN_All_modelx2')
        pil_image_d2 = array_to_img(image_d2)
        self.image = upscale_image(model, pil_image_d2)
        self.image = img_to_array(self.image).astype('uint8')

        modelx4 = tf.keras.models.load_model(os.getcwd() + '\\ESPCN_modelx4')
        # modelx4 = tf.keras.models.load_model(os.getcwd()+'\\SRDN_All_modelx4')
        pil_image_d4 = array_to_img(image_d4)
        self.imagex4 = upscale_image(modelx4, pil_image_d4)
        self.imagex4 = img_to_array(self.imagex4).astype('uint8')
        showImage2(self)

        # Ảnh sinh ra thì gán vào biến 'self.image' và phải có định dạng là numpy array
        ## câu lệnh chuyển từ pil image sang numpy array image
        # opencvImage = cv2.cvtColor(numpy.array(pil_image), cv2.COLOR_RGB2BGR)
        # pass

def segmentImg(self, image, itemPath):
    encoder = "vgg16"
    img1 = image
    def convert_to_tensor(x, **kwargs):
        return x.transpose(2, 0, 1).astype("float32")

    encoder_wts = "imagenet"
    preprocess_func = smp.encoders.get_preprocessing_fn(encoder, encoder_wts)

    device = "cuda"
    print(os.getcwd() +"\\model_resnet50_fold2.pth")
    best_model = torch.load(os.getcwd() +"\\model_resnet50_fold2.pth")

    transform = albumentations.Compose([
        albumentations.Resize(height=224, width=224, interpolation=Image.BILINEAR),
        albumentations.Lambda(image=preprocess_func),
        albumentations.Lambda(image=convert_to_tensor)
    ])
    image = Image.open(itemPath)
    image = np.array(image)
    augmentations = transform(image=image)
    image = augmentations["image"]
    print(image)
    x_tensor = torch.from_numpy(image)
    x_tensor = x_tensor.to(device).unsqueeze(0)
    pr_mask = best_model.predict(x_tensor)
    pr_mask = pr_mask.squeeze().cpu().numpy().round()
    res = (pr_mask - pr_mask.min()) / (pr_mask.max() - pr_mask.min() + 1e-8)
    pr_mask = (pr_mask * 255).astype(np.uint8)
    pr_mask = cv2.resize(pr_mask, (1280, 995))  # 960, 1280


    cv2.imwrite("mask.jpg", pr_mask)
    ret2, binary = cv2.threshold(pr_mask, 127, 255, cv2.THRESH_BINARY)
    contour, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img1, contour, -7, (0, 255, 0), 5)
    self.imgSeg = img1
    cv2.imwrite("demo.jpg",self.imgSeg)

    showImageSegment(self)