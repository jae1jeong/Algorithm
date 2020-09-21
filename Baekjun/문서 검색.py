document,word = str(input()),str(input())
index,result = 0,0

while len(document) - index >= len(word):
    if document[index:index+len(word)] == word: # 문서에서 보고 있는 단어가 찾고자 하는 단어인 경우
        result += 1
        index += len(word)
    else:
        index += 1
print(result)

