import openpyxl # openpyxl 모듈 불러오기

wb = openpyxl.load_workbook('./sample.xlsx')
sheet = wb['Sheet1']
for row in sheet.iter_rows(min_row=2):
    for cell in row:
        print(cell.value)
    print('-' * 10)
wb.close()