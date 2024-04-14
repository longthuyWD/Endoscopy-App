import sys

from Function.cleanness_dialog import *
from Function.cut_dialog import *
# from Function.export_dicom import *
from Function.generate_dialog import *
from Function.opencv_readpb import *
from Function.resize_dialog import *
from GUI.ui_AppGUI import *
import pandas as pd


class MainWindow(QMainWindow):
    evaluate = [['anh', 'point x2', 'description x2', 'point x4', 'description x4']]
    def __init__(self):
        QMainWindow.__init__(self) 
        self.ui = Ui_Cleanliness_Check()
        self.ui.setupUi(self)

        self.setWindowTitle("Cleanliness Check App")

        ### setup befor running
        self.ui.tabWidget.setCurrentIndex(0)
        self.mask = cv2.imread(r"Mask/mask.jpg")
        self.all = False
        self.applyMask = False
        self.autoLoadInfor = False
        self.imageDest = QImage()
        self.dir_ = 'D:\\'
        self.xStart = 0
        self.yStart = 0
        self.rect = QRect(0, 0, 1280, 960)
        self.threshold = 0.3
        self.uNet = read_pb_file('Function/unet_bb_rgb_small.pb')
        #self.ui.graphicsView2.hide()
        #self.ui.sourceImage.hide()
        #self.ui.destinationImage.hide()
        #self.ui.tag.hide()
        self.tab = 0

        ### button clicked
        self.ui.fileList.itemClicked.connect(self.fileListClicked)
        self.ui.generateList.itemClicked.connect(self.generateListClicked)
        self.ui.cropList.itemClicked.connect(self.cropListClicked)
        self.ui.superResolutionList.itemClicked.connect(self.superResolutionListClicked)
        self.ui.segmentList.itemClicked.connect(self.segmentListClicked)
        self.ui.evaluateList.itemClicked.connect(self.superResolutionListClicked2)
        self.ui.cleanlinessList.itemClicked.connect(self.cleanlinessListClicked)
        # self.ui.dicomList.itemClicked.connect(self.dicomListClicked)
        # self.ui.evaluateList.itemClicked.connect(self.evaluateListClicked)
        self.ui.treeView.clicked.connect(self.treeViewClicked)
        self.ui.tabWidget.tabBarClicked.connect(self.tabClicked)
        # self.ui.btnNext.clicked.connect(writeExcel(self))
        self.ui.SR2.clicked.connect(lambda: state(self, '2'))
        self.ui.SR4.clicked.connect(lambda: state(self, '4'))
        self.ui.SR8.clicked.connect(lambda: state(self, '8'))

        self.ui.worstx2.clicked.connect(lambda: state(self, '1 worst'))
        self.ui.worstx4.clicked.connect(lambda: statex4(self, '1 worst'))
        self.ui.poorx2.clicked.connect(lambda: state(self, '2 poor'))
        self.ui.poorx4.clicked.connect(lambda: statex4(self, '2 poor'))
        self.ui.goodx2.clicked.connect(lambda: state(self, '3 good'))
        self.ui.goodx4.clicked.connect(lambda: statex4(self, '3 good'))
        self.ui.betterx2.clicked.connect(lambda: state(self, '4 better'))
        self.ui.betterx4.clicked.connect(lambda: statex4(self, '4 better'))
        self.ui.excellentx2.clicked.connect(lambda: state(self, '5 excellent'))
        self.ui.excellentx4.clicked.connect(lambda: statex4(self, '5 excellent'))

        self.ui.btnNextx4.clicked.connect(self.evaluateSR)
        ### add graphic view, graphic scene
        self.graphicsScene1 = QGraphicsScene()
        self.graphicsScene2 = QGraphicsScene()
        self.graphicsScene3 = QGraphicsScene()

    def tabClicked(self, tab):
        self.tab = tab
        if self.tab == 5:
            self.ui.gVx2.show()
            self.ui.gVx4.show()
            self.ui.frame_1.show()
            self.ui.frame_6.show()
            self.ui.frame_4.show()
            self.ui.frame_5.show()
            self.ui.sourceImage.show()
            self.ui.destinationImage.show()
            self.ui.widget_2.show()
            showImage(self)

        else:
            self.ui.gVx2.hide()
            self.ui.gVx4.hide()
            self.ui.sourceImage.hide()
            self.ui.destinationImage.hide()
            self.ui.frame_4.hide()
            self.ui.frame_5.hide()
            self.ui.frame_1.hide()
            self.ui.frame_6.hide()
            self.ui.widget_2.hide()

        if self.tab == 6:
            #self.ui.tag.show()
            self.autoLoadInfor = True
            showImage(self)
        else:
            #self.ui.tag.hide()
            self.autoLoadInfor = False

        if self.tab == 1:
            self.beforeCrop = self.image

        if self.tab == 3:
            self.beforeResize = self.image
            self.ui.SR2.show()
            self.ui.SR4.show()
            self.ui.SR8.show()
        else:
            self.ui.SR2.hide()
            self.ui.SR4.hide()
            self.ui.SR8.hide()
        # if self.tab == 4:
        #     self.beforeCheckCleanliness = self.image


    def treeViewClicked(self, index):
        print(index.row())
        print(type(index))
        self.index1 = index
        self.stt = index.row()
        self.itemPath = index.model().filePath(index)
        self.image = cv2.imread(self.itemPath)
        print(self.itemPath)
        self.imageName = os.path.basename(self.itemPath)
        if self.tab == 1:
            self.beforeCrop = self.image
        if self.tab == 3:
            self.beforeResize = self.image
        if self.tab == 4:
            self.beforeCheckCleanliness = self.image
        if self.autoLoadInfor == True:
            loadMetaData(self, self.imageName)
        showImage(self)

    def fileListClicked(self, item):
        if item.text() == 'Open folder':
            openFolder(self, 'image')
            displayTreeFolder(self)
        if item.text() == 'Open file':
            openFile(self, 'image')
            showImage(self)

    def cropListClicked(self, item):
        if item.text() == 'Cut Infor':
            cutImage(self)
        if item.text() == 'Use Mask':
            cutMask(self, self.mask)
        if item.text() == 'Config':
            showCutDialog(self)
        if item.text() == 'Reset':
            self.image = self.beforeCrop
            showImage(self)
        if item.text() == 'Apply':
            cutImage(self)
        if item.text() == 'Save':
            openFolder(self, 'image')
            createFolder(self, self.folderPath, 'Ket qua cat anh')
            saveFol = os.path.join(self.folderPath, 'Ket qua cat anh')
            saveFile(self, self.imageName, saveFol)
        if item.text() == 'All folder':
            openFolder(self, 'image')
            # createFolder(self, self.folderPath, 'Ket qua cat anh')
            # saveFol = os.path.join(self.folderPath, 'Ket qua cat anh')
            saveFol = chooseFolder(self)
            cutFolder(self, self.infoList, saveFol)

    def generateListClicked(self, item):
        if item.text() == 'Config':
            showGenerateDialog(self)
        if item.text() == 'Apply':
            applyMethod(self, self.image)
        if item.text() == 'Save':
            openFolder(self, 'image')
            createFolder(self, self.folderPath, 'Ket qua sinh anh')
            saveFol = os.path.join(self.folderPath, 'Ket qua sinh anh')
            saveDestImage(self, self.imageName, saveFol)
        if item.text() == 'All Folder':
            openFolder(self, 'image')
            createFolder(self, self.folderPath, 'Ket qua sinh anh {}'.format(self.mode))
            saveFol = os.path.join(self.folderPath, 'Ket qua sinh anh {}'.format(self.mode))
            generateFolder(self, self.infoList, saveFol)

    def superResolutionListClicked(self, item):
        if item.text() == 'Config':
            showResizeDialog(self)
        if item.text() == 'Apply':
            resizeImage(self, self.image)
        if item.text() == 'Reset':
            self.image = self.beforeResize
            showImage(self)
        if item.text() == 'Save':
            openFolder(self, 'image')
            createFolder(self, self.folderPath, 'Ket qua chuan hoa anh')
            saveFol = os.path.join(self.folderPath, 'Ket qua chuan hoa anh')
            saveFile(self, self.imageName, saveFol)
        if item.text() == 'All Folder':
            openFolder(self, 'image')
            # createFolder(self, self.folderPath, 'Ket qua chuan hoa anh')
            # saveFol = os.path.join(self.folderPath, 'Ket qua chuan hoa anh')
            saveFol = chooseFolder(self)
            resizeFolder(self, self.infoList, saveFol)

    def superResolutionListClicked2(self, item):
        if item.text() == 'Config':
            showResizeDialog(self)
        if item.text() == 'Apply':
            resizeImagex4(self, self.image)
        if item.text() == 'Reset':
            self.image = self.beforeResize
            showImage(self)
        if item.text() == 'Save':
            openFolder(self, 'image')
            createFolder(self, self.folderPath, 'Ket qua chuan hoa anh')
            saveFol = os.path.join(self.folderPath, 'Ket qua chuan hoa anh')
            saveFile(self, self.imageName, saveFol)
        if item.text() == 'All Folder':
            openFolder(self, 'image')
            # createFolder(self, self.folderPath, 'Ket qua chuan hoa anh')
            # saveFol = os.path.join(self.folderPath, 'Ket qua chuan hoa anh')
            saveFol = chooseFolder(self)
            resizeFolder(self, self.infoList, saveFol)


    def cleanlinessListClicked(self, item):
        if item.text() == 'Config':
            showCleannessDialog(self)
        if item.text() == 'Apply':
            if checkImageShape(self):
                self.image = self.beforeCheckCleanliness
                cleannesCheck(self)
            else:
                mes(self, None, 'Please remove patient information and resize to 1280x960 image!' )
        if item.text() == 'Reset':
            self.image = self.beforeCheckCleanliness
            showImage(self)
        if item.text() == 'Save':
            openFolder(self, 'image')
            createFolder(self, self.folderPath, 'Ket qua danh gia sach')
            saveFol = os.path.join(self.folderPath, 'Ket qua danh gia sach')
            saveFile(self, self.imageName, saveFol)
        if item.text() == 'All Folder':
            openFolder(self, 'image')
            # createFolder(self, self.folderPath, 'Ket qua danh gia sach')
            # saveFol = os.path.join(self.folderPath, 'Ket qua danh gia sach')
            saveFol = chooseFolder(self)
            checkFolder(self, self.infoList, saveFol)

    # def dicomListClicked(self, item):
    #     if item.text() == 'Meta Data':
    #         openFile(self, 'excel')
    #         try:
    #             loadMetaData(self, self.imageName)
    #         except:
    #             pass
    #     if item.text() == 'Export':
    #         exportDicom(self, self.image, self.imageName)
    #     if item.text() == 'All Folder':
    #         openFolder(self, 'image')
    #         createFolder(self, self.folderPath, 'Anh dicom')
    #         saveFol = os.path.join(self.folderPath, 'Anh dicom')
    #         # saveFol = chooseFolder(self)
    #         exportAllFolder(self, self.infoList, saveFol)

    def evaluateListClicked(self, item):
        if item.text() == 'Open Folder':
            openFolder(self, 'image')
            displayTreeFolder(self)
        if item.text() == 'Meta Data':
            openFile(self, 'excel')

    def evaluateSR(self):

        self.datax2 = []
        self.datax2.append(str(self.imageName[:-4]))
        self.datax2.append(str(self.state[0]))
        self.datax2.append(str(self.ui.descriptionx2.toPlainText()))
        self.datax2.append(str(self.statex4[0]))
        self.datax2.append(str(self.ui.descriptionx4.toPlainText()))
        self.evaluate.append(self.datax2)
        rs = pd.DataFrame(self.evaluate)
        rs.to_excel(os.getcwd()+"\\result.xlsx")


        # print(self.state)
        # print(self.ui.descriptionx2.toPlainText())
        #
        # print(self.datax2)
        # print(self.evaluate)

        print("infor: %s" % self.infoList)
        print("index: %s" %self.index1)
        for fileInfo in self.infoList:
            print(fileInfo)
        #     # if dialog.canceled == True:
        #     #     break
        #     absPath = fileInfo.absoluteFilePath()
        #     absName = os.path.basename(absPath)
        #     self.image = cv2.imread(absPath)
        #     dialog.setValue(i)
        #     dialog.setLabelText(absName)
        #     i += 1
        #     applyMethod(self, self.image)
        #     saveDestImage(self, absName, saveFol)
    def segmentListClicked(self, item):
        if item.text() == 'Config':
            showResizeDialog(self)
        if item.text() == 'Apply':
            segmentImg(self, self.image, self.itemPath)
        if item.text() == 'Reset':
            self.image = self.beforeResize
            showImage(self)
        if item.text() == 'Save':
            openFolder(self, 'image')
            createFolder(self, self.folderPath, 'Ket qua khoanh vung anh')
            saveFol = os.path.join(self.folderPath, 'Ket qua khoanh vung anh')
            saveFile(self, self.imageName, saveFol)
        if item.text() == 'All Folder':
            openFolder(self, 'image')
            # createFolder(self, self.folderPath, 'Ket qua chuan hoa anh')
            # saveFol = os.path.join(self.folderPath, 'Ket qua chuan hoa anh')
            saveFol = chooseFolder(self)
            resizeFolder(self, self.infoList, saveFol)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
