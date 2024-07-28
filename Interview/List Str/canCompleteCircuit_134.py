import time
from typing import List

#
# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         L = len(gas)
#         gas_tank = 0
#         if sum(cost) > sum(gas):    # 若总消耗大于补充，直接 -1
#             return -1
#
#         for i in range(L):
#             gas_tank += gas[i] - cost[i]
#             if gas_tank <= 0:       # 做第一次判断，若该位置没办法到达下一位置，直接跳过该位置
#                 gas_tank = 0
#                 i += 1
#                 continue
#             gas_tank += gas[i + 1]  # 抵达下一位置获取补充油箱
#         return i

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        curSum = 0
        totalSum = 0
        for i in range(len(gas)):
            curSum += gas[i] - cost[i]
            totalSum += gas[i] - cost[i]
            if curSum < 0:
                curSum = 0
                start = i + 1
        if totalSum < 0: return -1
        return start



if __name__ == '__main__':
    s_time = time.time()
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(Solution().canCompleteCircuit(gas, cost))
    e_time = time.time()
    a_time = e_time - s_time
    print(a_time)
