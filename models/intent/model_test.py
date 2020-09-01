import tensorflow as tf
from tensorflow.keras.models import Model, load_model
from tensorflow.keras import preprocessing

intent_labels = {0: "인사", 1: "욕설", 2: "주문", 3: "예약", 4: "기타"}

# 의도 분류 모델 불러오기
model = load_model('intent_model.h5')

query = "오늘 탕수육 주문 가능한가요?"
query = "안녕하세요?"
from utils.Preprocess import Preprocess
p = Preprocess(word2index_dic='../../train_tools/dict/chatbot_dict.bin',
               userdic='../../utils/user_dic.tsv')
pos = p.pos(query)
keywords = p.get_keywords(pos, without_tag=True)
seq = p.get_wordidx_sequence(keywords)
sequences = [seq]

# 단어 시퀀스 벡터 크기
from config.GlobalParams import MAX_SEQ_LEN
padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')

predict = model.predict(padded_seqs)
predict_class = tf.math.argmax(predict, axis=1)
print(query)
print("의도 예측 점수 : ", predict)
print("의도 예측 클래스 : ", predict_class.numpy())
print("의도  : ", intent_labels[predict_class.numpy()[0]])

