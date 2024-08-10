# @Time :2024/9/14 8:52

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        res = []
        i = 0

        for i in range(min(l1, l2)):
            res.append(word1[i])
            res.append(word2[i])

        if i < l1:
            res.append(word1[i + 1:])
        if i < l2:
            res.append(word2[i + 1:])

        return ''.join(res)

if __name__ == '__main__':
    word1 = "ab"
    word2 = "pqrs"
    print(Solution().mergeAlternately(word1, word2))