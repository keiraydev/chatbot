try:
    a = 10
    b = 'zero'  # 'zero'를 0으로 바꾸고 실행하면 예외 처리가 달라집니다.
    c = a / b
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
