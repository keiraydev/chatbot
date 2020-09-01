def ngram(s, num):
    res = []
    slen = len(s) - num + 1
    for i in range(slen):
        ss = s[i:i+num]
        res.append(ss)
    return res



def diff_ngram(sa, sb, num):
    a = ngram(sa, num)
    print(a)
    b = ngram(sb, num)
    print(b)

    r = []
    cnt = 0
    for i in a:
        if i in b:
            cnt += 1
            r.append(i)

    return cnt / len(a), r


# a = '오늘 강남에서 맛있는 스파게티를 먹었다.'
# b = '강남에서 먹었던 오늘의 스파게티는 맛있었다.'
#
# r2, word2 = diff_ngram(a, b, 2)
# print('2-gram:', r2, word2)
# # result : 2-gram: 0.7619047619047619 ['오늘', '강남', '남에', '에서', '서 ', ' 맛', '맛있', '는 ', ' 스', '스파', '파게', '게티', ' 먹', '먹었', '었다', '다.']
#
# r3, word3 = diff_ngram(a, b, 3)
# print('3-gram:', r3, word3)
# # result : 3-gram: 0.45 ['강남에', '남에서', '에서 ', ' 맛있', ' 스파', '스파게', '파게티', ' 먹었', '었다.']


sentence1 = '1661년 6월 뉴턴 선생님 제안 트리니티 입학'
sentence2 = '2020년 6월 뉴턴 선생님 제안 대학교 입학'
r2, word2 = diff_ngram(sentence1, sentence2, 2)
print('2-gram:', r2, word2)