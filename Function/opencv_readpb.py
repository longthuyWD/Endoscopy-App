import cv2
from cv2 import dnn
import numpy as np


def call_otsu_threshold(image, is_reduce_noise=False):
    # Apply GaussianBlur to reduce image noise if it is required
    if is_reduce_noise:
        image = cv2.GaussianBlur(image, (5, 5), 0)
    # Optimal threshold value is determined automatically.
    otsu_threshold, image_result = cv2.threshold(
        image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,
    )
    return image_result


def read_pb_file(pbPath):
    uNet = dnn.readNet(pbPath)
    uNet.setPreferableBackend(dnn.DNN_BACKEND_OPENCV)
    uNet.setPreferableTarget(dnn.DNN_TARGET_CPU)
    return uNet

def output_seg(uNet, img, w=1280, h=960):
    imagemask = cv2.imread("Mask/mask.jpg")
    # cv2.imshow('Imagemask',imagemask)
      
    # counting the number of pixels
    number_of_white_pix = np.sum(imagemask == 255)
    number_of_black_pix = np.sum(imagemask == 0)
    ratio = number_of_white_pix/(number_of_white_pix + number_of_black_pix)
    # img = cv2.imread(imgPath)
    inputBlob = dnn.blobFromImage(image=img, scalefactor = 1/255.0, size=(w, h), swapRB=True, crop=False)
    uNet.setInput(inputBlob)
    out = uNet.forward()
    out = np.squeeze(out)
    out*=255
    out = out.astype(np.uint8)
    out = call_otsu_threshold(out)
    perOut = out/255
    #cv2.imshow('x', perOut)
    percentage = perOut.sum()/(perOut.shape[0]*perOut.shape[1]*ratio)
    # percentage = perOut.sum()/number_of_white_pix

    return out, percentage


def draw_contours(img, mask, color=(255, 255, 0), penSize=2):
    imgN = img.copy()
    contours, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    imgDraw = cv2.drawContours(imgN, contours, -1, color, penSize, cv2.LINE_AA)
    return imgDraw
