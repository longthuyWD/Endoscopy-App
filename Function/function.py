import os
import cv2
import numpy as np
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from Function import *

###########################################################################################################
def displayTreeFolder(self):
    self.ui.treeView.show()
    self.model = QFileSystemModel()
    self.model.setRootPath(self.folderPath)
    self.ui.treeView.setModel(self.model)
    self.ui.treeView.setRootIndex(self.model.index(self.folderPath))
    self.ui.treeView.setColumnWidth(0, 250)
    self.ui.treeView.setAlternatingRowColors(True)
    self.ui.treeView.header().showSection(0)
    self.ui.treeView.header().hideSection(1)
    self.ui.treeView.header().showSection(2)
    self.ui.treeView.header().hideSection(3)

###############################################################################################################
def openFolder(self, filters):
    self.dir_ = QFileDialog.getExistingDirectory(None, 'Select a folder:', self.dir_, QFileDialog.ShowDirsOnly)
    
    if self.dir_ != '':
        loadDir = QDir(self.dir_)
        loadDir.setNameFilters(['*.jpg', '*.JPG', '*.png', '*.PNG'])
        self.infoList = loadDir.entryInfoList()
        self.folderPath = str(self.dir_)
    print(self.infoList)

def chooseFolder(self):
    dir_ = QFileDialog.getExistingDirectory(None, 'Select a folder to save images:', self.dir_, QFileDialog.ShowDirsOnly)
    return dir_

def createFolder(self, path, nameFolder):
    resFol = os.path.join(path, nameFolder)
    if not os.path.isdir(resFol):
        os.mkdir(resFol)

def openFile(self, filters):
    _filter = applyFilters(self, filters)
    dir_ = QFileDialog.getOpenFileName(None, 'Select a folder:', self.dir_, _filter)
    self.dir_ = dir_[0]
    if filters == 'image':
        if self.dir_ != '':
            self.itemPath = str(self.dir_)
            self.folderPath = os.path.abspath(os.path.join(self.itemPath, os.pardir))
            self.imageName = os.path.basename(self.itemPath)
            self.image = cv2.imread(self.itemPath)
            if self.autoLoadInfor == True:
                loadMetaData(self)
            for i in range(3):
                self.ui.treeView.header().hideSection(i)
    if filters == 'excel':
        if self.dir_ !='':
            self.excelPath = str(self.dir_)
            self.autoLoadInfor = True

def applyFilters(self, filters):
    if filters == 'image':
        _filter = ('*.png *.PNG *.jpg *.JPG')
    if filters == 'excel':
        _filter = ('*.xlsx *.csv')
    if filters == 'dicom':
        _filter = ('*.dcm')
    return _filter

#########################################################################################################
def showImage(self):
    image = cv2qpixmap(self, self.image)
    self.graphicsScene1.clear()
    item = QGraphicsPixmapItem(image)
    self.graphicsScene1.addItem(item)
    self.graphicsScene1.setSceneRect(0, 0, image.width(), image.height())
    self.ui.gVSource.setScene(self.graphicsScene1)
    self.ui.gVSource.fitInView(self.graphicsScene1.sceneRect(), Qt.KeepAspectRatio)
    changeSpinBox(self)

def showImage2(self):
    image = cv2qpixmap(self, self.image)
    self.graphicsScene2.clear()
    item = QGraphicsPixmapItem(image)
    self.graphicsScene2.addItem(item)
    self.graphicsScene2.setSceneRect(0, 0, image.width(), image.height())
    self.ui.gVx2.setScene(self.graphicsScene2)
    self.ui.gVx2.fitInView(self.graphicsScene2.sceneRect(), Qt.KeepAspectRatio)
    changeSpinBox(self)

    imagex4 = cv2qpixmap(self, self.imagex4)
    self.graphicsScene3.clear()
    itemx4 = QGraphicsPixmapItem(imagex4)
    self.graphicsScene3.addItem(itemx4)
    self.graphicsScene3.setSceneRect(0, 0, imagex4.width(), imagex4.height())
    self.ui.gVx4.setScene(self.graphicsScene3)
    self.ui.gVx4.fitInView(self.graphicsScene3.sceneRect(), Qt.KeepAspectRatio)
    changeSpinBox(self)

def showImageSegment(self):
    image = cv2qpixmap(self, self.imgSeg)
    self.graphicsScene1.clear()
    item = QGraphicsPixmapItem(image)
    self.graphicsScene1.addItem(item)
    self.graphicsScene1.setSceneRect(0, 0, image.width(), image.height())
    self.ui.gVSource.setScene(self.graphicsScene1)
    self.ui.gVSource.fitInView(self.graphicsScene1.sceneRect(), Qt.KeepAspectRatio)
    changeSpinBox(self)

def showImageGenerated(self):
    image = cv2qpixmap(self, self.imageDest)
    self.graphicsScene2.clear()
    item = QGraphicsPixmapItem(image)
    self.graphicsScene2.addItem(item)
    self.graphicsScene2.setSceneRect(0, 0, image.width(), image.height())
    self.ui.gVx2.setScene(self.graphicsScene2)
    self.ui.gVx2.fitInView(self.graphicsScene2.sceneRect(), Qt.KeepAspectRatio)

def saveFile(self, imageName, saveFol):
    cv2.imwrite(os.path.join(saveFol, imageName), self.image)
    if self.all == False:
        mes(self, None, 'You save file successfully in folder: ' + saveFol)

def changeSpinBox(self):
    self.imageWidth = self.image.shape[1]
    self.imageHeight = self.image.shape[0]
    self.ratio = self.imageWidth / self.imageHeight
    self.ui.xEnd.setValue(self.imageWidth)
    self.ui.yEnd.setValue(self.imageHeight)

def cv2qpixmap(self, cv_img):
    rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    h, w, ch = rgb_image.shape
    bytes_per_line = ch * w
    convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
    return QPixmap.fromImage(convert_to_Qt_format)    # when convert to qimage format, the image not show up correctly

def mes(self, title, text):
    msgBox = QMessageBox()
    msgBox.setWindowTitle(title)
    msgBox.setText(text)
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()

def checkImageShape(self):
    if self.image.shape == (960, 1280, 3):
        return True
    else:
        return False

