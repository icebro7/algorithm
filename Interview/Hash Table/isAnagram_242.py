from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = Counter(s).most_common()
        t_count = Counter(t).most_common()

        for i in range(len(s_count)):
            if s_count[i] not in t_count:
                return False
        return True


if __name__ == '__main__':
    s = "ab"
    t = "ba"
    print(Solution().isAnagram(s, t))
