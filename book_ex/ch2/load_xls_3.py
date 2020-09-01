import openpyxl # openpyxl 모듈 불러오기

wb = openpyxl.load_workbook('./sample.xlsx')
sheet = wb['Sheet1']
cells = sheet['A2':'C3']
for row in cells:
    for cell in row:
        print(cell.value)
    print('-' * 10)
wb.close()