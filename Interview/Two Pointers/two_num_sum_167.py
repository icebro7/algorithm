from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        L = len(numbers) -1
        n = 0

        while n<L:
            numsum = numbers[n] + numbers[L]    #首先进行一次计算
            if numsum == target:    #若符合则记录，因为只有一个符合的答案，所以符合直接break
                res.append(n + 1)
                res.append(L + 1)
                break
            elif numsum > target:   #若数过大，则移动尾端的指针,list已经过排序
                L -= 1
            else:
                n += 1

        return  res
#
#
# if __name__ == '__main__':
#     numbers = [2,7,11,15]
#     target = 9
#     print(Solution().twoSum(numbers,target))


