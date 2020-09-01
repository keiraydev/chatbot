from konlpy.tag import Okt

# Okt 형태소 분석기 객체 생성
okt = Okt()
text = "아버지가 방에 들어갑니다."

# 형태소 추출
morphs = okt.morphs(text)
print(morphs)

# 형태소와 품사 태그 추출
pos = okt.pos(text)
print(pos)

# 명사만 추출
nouns = okt.nouns(text)
print(nouns)

# 정규화, 어구 추출
text = "오늘 날씨가 좋아욬ㅋㅋ"
print(okt.normalize(text))
print(okt.phrases(text))