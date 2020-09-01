from konlpy.tag import Komoran

komoran = Komoran()
text = "우리 챗봇은 엔엘피를 좋아해."
pos = komoran.pos(text)
print(pos)