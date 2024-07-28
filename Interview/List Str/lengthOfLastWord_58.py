import time


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        L = len(s)
        num = 0
        if L == 0:
            return 0
        for i in range(L):
            temp = s[-i-1]
            if temp == " " and num == 0:
                continue
            num += 1
            if temp == " ":
                return num - 1
        return num

if __name__ == '__main__':
    s_time = time.time()
    s = "luffy is still joyboy"
    print(Solution().lengthOfLastWord(s))
    e_time = time.time()
    a_time = e_time - s_time
    print(a_time)