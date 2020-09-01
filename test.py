from utils.Preprocess import Preprocess
from models.intent.IntentModel import IntentModel

p = Preprocess(word2index_dic='train_tools/dict/chatbot_dict.bin',
               userdic='utils/user_dic.tsv')

intent = IntentModel(model_name='models/intent/intent_model.h5', proprocess=p)
query = "오늘 탕수육 주문 가능한가요?"
c = intent.predict_class(query)
print(intent.labels[c])