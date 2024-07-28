class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            if n in visited:    # 如果该数已访问过
                return False
            visited.add(n)
            n = sum([digit ** 2 for digit in map(int, str(n))])

        return True

if __name__ == '__main__':
    n = 6523599898989898989889898
    print(Solution().isHappy(n))
