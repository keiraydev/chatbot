import pandas as pd

# sample.xlsx 엑셀 파일 읽어오기
user_list = pd.read_excel('sample.xlsx', sheet_name='Sheet1')
print(user_list)