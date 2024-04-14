import openpyxl
path = 'D:/Lab_HAR/GUI_endoscopy/full images/IGH AINN20 DICOM 220322.xlsx'
wb = openpyxl.load_workbook(path)
ws = wb.active

for row in ws.iter_rows():
    if row[0].value == 'PKHL_06 210818_191120_BN007_003':
        for cell in row:
            print(cell.value)