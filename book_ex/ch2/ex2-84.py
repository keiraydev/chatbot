import pickle

f = open('setting.txt', 'wb')
try:
    setting = [ {'title': 'python program'}, {'author': 'Kei'} ]
    pickle.dump(setting, f)
except Exception as e:
    print(e)
finally:
    f.close()

