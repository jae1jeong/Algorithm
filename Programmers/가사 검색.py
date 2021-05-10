class Trie:

    def __init__(self):
        self.child = dict()
        self.count = 0
    
    def insert(self,string):
        cur = self
        for ch in string:
            cur.count += 1
            if ch not in cur.child:
                cur.child[ch] = Trie()
            cur = cur.child[ch]
        # 리프노드도 카운트 + 1
        cur.count += 1

    def search(self,string):
        cur = self
        for st in string:
            if st == "?":
                return cur.count
            if st not in cur.child:
                return 0
            cur = cur.child[st]
        # 물음표는 항상 있기 때문에 끝까지 내려오는 경우는 없음
        return cur.count
            



def solution(words, queries):
    answer = []
    TrieRoot = [Trie() for _ in range(10000)]
    ReTrieRoot = [Trie() for _ in range(10000)]

    for string in words:
        TrieRoot[len(string)-1].insert(string)
        ReTrieRoot[len(string)-1].insert(string[::-1])
    
    for string in queries:
        if string[0] != "?":
            answer.append(TrieRoot[len(string)-1].search(string))
        else:
            answer.append(ReTrieRoot[len(string)-1].search(string[::-1]))

    return answer
    



wds = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
qur = ["fro??", "????o", "fr???", "fro???", "pro?"]

print([Trie() for _ in range(2)])
print([Trie()] * 2) # 똑같은 객체가 됨 