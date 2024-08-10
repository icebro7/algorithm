# @Time :2024/9/14 9:55

class Solution:
    def reverseVowels(self, s: str) -> str:
        l = len(s)
        yy = []

        for i in range(l):
            if s[i] in 'aeiouAEIOU':
                yy.append(s[i])
        yy.reverse()
        res = []
        j = 0
        for i in range(l):
            if s[i] in 'aeiouAEIOU':
                res.append(yy[j])
                j += 1
            else:
                res.append(s[i])
        return ''.join(res)
if __name__ == '__main__':
    s = "hello"
    print(Solution().reverseVowels(s))