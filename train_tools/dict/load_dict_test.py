import pickle

f = open("chatbot_dict.bin", "rb")
word_index = pickle.load(f)
f.close()

print(word_index['OOV'])
print(word_index['오늘'])
print(word_index['주문'])
print(word_index['삼선볶음밥'])
print(word_index['1시'])
