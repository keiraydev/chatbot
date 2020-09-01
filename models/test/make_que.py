import csv

word_file = 'keyword.csv'
sent_file = '주문조합.csv'

with open(word_file, mode='r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        word = str(row[0]).strip()

        with open(sent_file, mode="r", encoding="utf-8") as qf:
            qreader = csv.reader(qf)
            for j, qrow in enumerate(qreader):
                q = word + ' ' + qrow[0].strip() + ',2'
                print(q)
