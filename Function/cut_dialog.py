from GUI.ui_CutDialog import *
from Function.function import *

def showCutDialog(self):
    self.dialog = QDialog()
    self.dialog.ui = Ui_CutDialog()
    self.dialog.ui.setupUi(self.dialog)

    self.x0 = self.dialog.ui.startX
    self.y0 = self.dialog.ui.startY
    self.w = self.dialog.ui.width
    self.h = self.dialog.ui.height
    self.state = 'custom'

    self.w.setPlaceholderText(str(self.imageWidth))
    self.h.setPlaceholderText(str(self.imageHeight))


    self.dialog.ui.custom.clicked.connect(lambda: state(self, 'custom'))
    self.dialog.ui.aspect.clicked.connect(lambda: state(self, 'aspect'))

    self.w.textChanged.connect(lambda: changeStateClicked(self))

    self.dialog.ui.btnConfirm.clicked.connect(lambda: confirmDialog(self))
    self.dialog.ui.btnCancel.clicked.connect(lambda: cancelDialog(self))
    self.dialog.exec_()

def confirmDialog(self):
    x1 = toNum(self, self.x0.text())
    y1 = toNum(self, self.y0.text())
    w = toNum(self, self.w.text())
    h = toNum(self, self.h.text())
    if w == 0:
        w = self.imageWidth
    if h == 0:
        h = self.imageHeight
    x2 = x1 + w
    y2 = y1 + h
    self.rect = QRect(x1, y1, x2, y2)
    self.dialog.close()

def cancelDialog(self):
    self.dialog.close()

def cutImage(self):
    self.imageCutted = self.image[self.rect.y() : self.rect.height() , self.rect.x() : self.rect.width()]
    self.image = self.imageCutted
    showImage(self)
    changeSpinBox(self)

def cutMask(self, mask):
    mask = cv2.resize(src=mask, dsize=(self.image.shape[1], self.image.shape[0]))
    thresh, mask = cv2.threshold(mask, thresh=128, maxval=1, type=cv2.THRESH_BINARY)
    self.imageOutput = self.image * mask
    self.image = self.imageOutput
    showImage(self)

def cutFolder(self, infoList, saveFol):
    self.all = True
    dialog = QProgressDialog('Loại bỏ thông tin bệnh nhân trên cả thư mục', 'Dừng chạy', 0, len(infoList))
    dialog.setWindowTitle('Loại bỏ thông tin')
    dialog.setWindowModality(Qt.WindowModal)
    i = 0
    for fileInfo in infoList:
        absPath = fileInfo.absoluteFilePath()
        absName = os.path.basename(absPath)
        self.image = cv2.imread(absPath)
        dialog.setValue(i)
        dialog.setLabelText(absName)
        i+=1
        cutImage(self)
        cutMask(self, self.mask)
        saveFile(self, absName, saveFol)
    mes(self, 'Notification!', 'You save ALL file successfully in folder: ' + saveFol)
    self.all = False


