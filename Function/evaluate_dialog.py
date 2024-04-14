import openpyxl

from Function.function import *

def writeExcel(self):
	if self.ui.level.currentText() == 'Choose...':
		mes(self, None, 'Please enter level!')
		print('1')
	else:
		print('2')
		wb = openpyxl.load_workbook(self.excelPath)
		ws = wb.active
		for row in ws.iter_rows():
		    if row[0].value == self.imageName[:-4]:
		        row[6].value == self.ui.level.text()
		        row[7].value == self.ui.description.text()