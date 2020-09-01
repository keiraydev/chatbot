# main1.py
# calc 모듈에서 add, mul 함수만 불러옴. main1.py와 같은 경로에 있어야 함
from calc import add, mul

a = add(10, 20) # calc 모듈의 add 함수
print("add = {}".format(a))
b = mul(10, 2) # calc 모듈의 mul 함수
print("add = {}".format(b))