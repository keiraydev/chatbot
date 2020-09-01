import csv
from konlpy.tag import Komoran
from random import  *

date_file = 'date.csv'
food_file = 'food.csv'
sent_file = '주문조합.csv'

komoran = Komoran(userdic='../../utils/user_dic.tsv')

file = open("새파일2.txt", 'w')
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
                    raw_q = ";"
                    res_q = '$'
                    line = ""
                    for i, s in enumerate(sentence):
                        raw_q += "{} ".format(s[0])
                        res_q += "{} ".format(s[0])
                        if s[1] == 'B_DT':
                            line += "{}\t{}\t{}\t{}\n".format(i + 1, s[0], 'NNG', s[1])
                        elif s[1] == 'B_FOOD':
                            line += "{}\t{}\t{}\t{}\n".format(i + 1, s[0], 'NNG', s[1])
                        else:
                            line += "{}\t{}\t{}\t{}\n".format(i + 1, s[0], s[2], s[1])

                    print(raw_q)
                    print(res_q)
                    print(line)
                    file.write(raw_q + "\n")
                    file.write(res_q + "\n")
                    file.write(line + "\n")

file.close()
exit()
with open(food_file, mode='r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        word = str(row[0]).strip()

        with open(sent_file, mode="r", encoding="utf-8") as qf:
            qreader = csv.reader(qf)
            for j, qrow in enumerate(qreader):
                question = word.strip() + ' ' + qrow[0].strip()
                question = question.replace(" ﻿", " ")
                raw_q = '; ' + question
                res_q = "$ <{}:FOOD>".format(word)+ ' ' + qrow[0].strip()
                pos = komoran.pos(question)

                lines += (raw_q + "\n")
                lines += (res_q + "\n")

                for i, p in enumerate(pos):
                    if i==0: tag = "B_FOOD"
                    else: tag = 'O'

                    line = "{}\t{}\t{}\t{}\n".format(i+1, p[0], p[1], tag)
                    lines += line
                lines += "\n"
            break
        break

# f = open("새파일.txt", 'w')
# f.write(lines)
# f.close()

print(lines)