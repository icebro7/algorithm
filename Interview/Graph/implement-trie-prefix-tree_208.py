# @Time :2024/9/6 9:28
class Trie:
    def __init__(self):
        self.words = set()
        self.prefixs = set()

    def insert(self, word: str) -> None:
        self.words.add(word)
        for i in range(len(word),0,-1):
            s = word[:i]
            if s in self.prefixs:
                break
            self.prefixs.add(s)

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefixs