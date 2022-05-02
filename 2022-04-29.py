def example(inp):
    answer = ""
    
    wordTable = []
    transform = []
    for word in inp.split():
        newWord = word[:]
        for table in wordTable:
            if table.lower() in newWord.lower():
                newWord = newWord.lower().replace(table.lower(), "")
                if len(newWord) > 0:
                    transform.append(newWord)
                break
        if len(newWord) == len(word):
            transform.append(newWord)
        for i in range(len(newWord)):
            for length in range(2 + i, len(newWord) + 1):
                wordTable.append(newWord[i:length])
        wordTable.sort(key=len, reverse=True)
    answer = " ".join(transform)
    return answer

res = example("A4c 강아지고양이 장난감 고양이임니다 a4C6 임니다 A4C") # A4c 강아지고양이 장난감 임니다 6
#res = example("차량용스마트폰 가정집스마트폰 기업용스마트폰")

print(res)
