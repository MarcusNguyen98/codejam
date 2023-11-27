import sys
input = sys.stdin.readline

temp = input().split()
N = int(temp[0])
Q = int(temp[1])

sentences = ['' for i in range(N)]
searches = ['' for i in range(Q)]
for i in range(N):
    sentences[i] = input()
    sentences[i] = sentences[i].replace('\n', '')
for i in range(Q):
    searches[i] = input()
    searches[i] = searches[i].replace('\n', '')


def search(sentence, search):
    lowerSentence = sentence.replace(' ', '').lower()
    lowerSearch = search.replace(' ', '').lower()

    findI = lowerSentence.find(lowerSearch)
    found = False
    if (findI >= 0):
        wordL = ''
        for word in sentence.split():
            wordL += word.lower()
            findWordInSearch = lowerSearch.find(wordL)
            if (findWordInSearch == -1 or findWordInSearch > 0):
                if wordL.find(lowerSearch) == 0:
                    found = True
                    break
                wordL = ''
                continue
            if (lowerSearch.find(wordL) == 0 and len(wordL) == len(lowerSearch)):
                found = True
                break
        
        return found
    else:
        return False

for i in range(Q):
    total = 0
    for j in range(N):
        ret = search(sentences[j], searches[i])
        if ret == True:
            total += 1
    print(total)