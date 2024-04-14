import pydicom
from pydicom.dataset import Dataset, FileDataset
from pydicom.uid import generate_uid
import numpy
import cv2
import openpyxl


from Function.function import *

def loadMetaData(self, imageName):
    wb = openpyxl.load_workbook(self.excelPath)
    ws = wb.active

    for row in ws.iter_rows():
        if row[0].value == imageName[:-4]:
            self.ui.patientName.setText(row[0].value)
            self.ui.seriesDescription.setText(row[1].value)
            self.ui.studyDate.setText(row[3].value) 
            self.ui.studyModality.setText(row[4].value)
            self.ui.studyDescription.setText(row[5].value)

def writeDicom(self, image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    self.ds = Dataset()
    self.ds.file_meta = Dataset()
    self.ds.file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRLittleEndian
    self.ds.file_meta.MediaStorageSOPClassUID = '1.2.840.10008.5.1.4.1.1.1.1'
    self.ds.file_meta.MediaStorageSOPInstanceUID = "1.2.3"
    self.ds.file_meta.ImplementationClassUID = "1.2.3.4"

    self.ds.PixelData = image

    self.ds.PatientName = self.ui.patientName.text()
    self.ds.PatientID = self.ui.patientID.text()
    self.ds.PatientBirthDate = self.ui.patientBirthDate.text()
    self.ds.PatientSex = self.ui.patientSex.text()
    self.ds.PatientAge = self.ui.patientAge.text()
    self.ds.PatientWeight = self.ui.patientWeight.text()
    self.ds.PatientAddress = self.ui.patientAddress.text()

    self.ds.StudyDate = self.ui.studyDate.text()
    self.ds.StudyTime = self.ui.studyTime.text()
    self.ds.StudyID = self.ui.studyID.text()
    self.ds.Modality = self.ui.studyModality.text()
    self.ds.StudyDescription = self.ui.studyDescription.text()

    self.ds.SeriesDate = self.ui.seriesDate.text()
    self.ds.SeriesTime = self.ui.seriesTime.text()
    self.ds.SeriesDescription = self.ui.seriesDescription.text()

    self.ds.Rows = image.shape[0]
    self.ds.Columns = image.shape[1]
    self.ds.PhotometricInterpretation = "RGB"
    
    self.ds.SamplesPerPixel = 3
    self.ds.BitsStored = 8
    self.ds.BitsAllocated = 8
    self.ds.HighBit = 7
    self.ds.PixelRepresentation = 0
    self.ds.PlanarConfiguration = 0
    self.ds.NumberOfFrames = 1

    self.ds.SOPClassUID = generate_uid()
    self.ds.SOPInstanceUID = generate_uid()
    self.ds.StudyInstanceUID = generate_uid()
    self.ds.SeriesInstanceUID = generate_uid()

    self.ds.is_little_endian = True
    self.ds.is_implicit_VR = False

def exportDicom(self,image, imageName):
    writeDicom(self, image)
    dicomfilename = imageName[0:30] + '.dcm'
    openFolder(self, ('dicom'))
    createFolder(self, self.folderPath, 'Anh dicom')
    saveFol = os.path.join(self.folderPath, 'Anh dicom')
    self.ds.save_as(os.path.join(saveFol, dicomfilename))
    mes(self, None, 'You save file successfully in folder: ' + saveFol)

def exportAllFolder(self, infoList, saveFol):
    self.all = True
    dialog = QProgressDialog('Chuyển các ảnh thành định dạng dicom', 'Dừng chạy', 0, len(infoList))
    dialog.setWindowTitle('Chuyển đổi')
    dialog.setWindowModality(Qt.WindowModal)
    i = 0
    for fileInfo in infoList:
        absPath = fileInfo.absoluteFilePath()
        absName = os.path.basename(absPath)
        self.image = cv2.imread(absPath)
        dialog.setValue(i)
        dialog.setLabelText(absName)
        i+=1
        try:
            loadMetaData(self, absName)
        except:
            pass
        writeDicom(self, self.image)
        dicomfilename = absName[0:30] + '.dcm'
        self.ds.save_as(os.path.join(saveFol, dicomfilename))
    mes(self, 'Notification!', 'You save ALL file successfully in folder: ' + saveFol)
    self.all = False
