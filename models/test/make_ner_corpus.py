import csv
from konlpy.tag import Komoran
from random import  *

date_file = 'date.csv'
food_file = 'food.csv'
sent_file = '주문조합.csv'

komoran = Komoran(userdic='../../utils/user_dic.tsv')

file = open("corpus.txt", 'w')

for cnt in range(5):
    with open(date_file, mode='r', encoding='utf-8-sig') as df:
        dr = csv.reader(df)
        for k, r in enumerate(dr):

            food_sel = randint(1, 243)
            with open(food_file, mode='r', encoding='utf-8-sig') as f:
                reader = csv.reader(f)

                for i, row in enumerate(reader):
                    if i != food_sel: continue

                    sel = randint(1, 155)
                    with open(sent_file, mode="r", encoding="utf-8") as qf:
                        qreader = csv.reader(qf)
                        for qi, qrow in enumerate(qreader):
                            if(qi != sel): continue

                            sentence = []
                            tmp = r[0].split(' ')
                            for t in tmp:
                                date = t.split(':')
                                sentence.append(tuple(date))

                            word = row[0].split(':')
                            sentence.append(tuple(word))

                            q = qrow[0]
                            q = q.replace('\ufeff', '')
                            pos = komoran.pos(q)
                            for p in pos:
                                x = (p[0], 'O', p[1])
                                sentence.append(x)
                            break

                        # 파일 저장
                        raw_q = ""
                        for i, s in enumerate(sentence):
                            raw_q += "{} ".format(s[0])

                        raw_q = "{}\t{}\t{}".format('0000', raw_q, 0)
                        print(raw_q)
                        file.write(raw_q + "\n")

file.close()