from GUI.ui_CleannessDialog import *
from Function.function import *
from Function.function_dialog import *
from Function.opencv_readpb import *

def showCleannessDialog(self):
    self.dialog = QDialog()
    self.dialog.ui = Ui_CleannessDialog()
    self.dialog.ui.setupUi(self.dialog)

    self.threshold = toNum(self, self.dialog.ui.threshold.text())
    self.dialog.ui.btnConfirm.clicked.connect(lambda: confirmCheck(self))

    self.dialog.exec_() 

def confirmCheck(self):
    self.dialog.close()

def cleannesCheck(self):
    mask, per = output_seg(self.uNet, self.image)
    self.imgDraw = draw_contours(self.image, mask)

    self.imageOutput = self.imgDraw
    self.image = self.imageOutput
    showImage(self)
    self.cleanRes = define_cleanliness(self, per, self.threshold)
    if self.all == False:
        mes(self, None, 'Ảnh sạch' if self.cleanRes else 'Ảnh không sạch')
    
def checkFolder(self, infoList, saveFol):
    self.all = True
    dialog = QProgressDialog('Đang đánh giá độ sạch trên toàn thư mục', 'Dừng chạy', 0, len(infoList))
    dialog.setWindowTitle('Đánh giá độ sạch trên thư mục')
    dialog.setWindowModality(Qt.WindowModal)
    i = 0
    for fileInfo in infoList:
        absPath = fileInfo.absoluteFilePath()
        absName = os.path.basename(absPath)
        self.image = cv2.imread(absPath)
        dialog.setValue(i)
        dialog.setLabelText(absName)
        i+=1
        cleannesCheck(self)
        res = 'Sạch' if self.cleanRes else 'Không sạch'
        createFolder(self, saveFol, 'Sach')
        createFolder(self, saveFol, 'Khong Sach')
        if res == 'Sạch':
            subFol = os.path.join(saveFol, 'Sach')
        else:
            subFol = os.path.join(saveFol, 'Khong Sach')
        saveFile(self, absName, subFol)
    mes(self, 'Notification!', 'You save ALL file successfully!')
    self.all = False


def define_cleanliness(self, per, threshold):
    if per < threshold:
        return True
    else:
        return False

