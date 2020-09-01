class SimpleObj:
    def __init__(self):
        print('call __init__()')

    def __del__(self):
        print('call __del__()')

obj = SimpleObj()
print('obj instance is alive...')
del obj