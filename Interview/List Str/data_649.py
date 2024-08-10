# @Time :2024/9/21 9:19
import collections


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = collections.deque(senate) # 玩家行动队列
        player_count = {'R':0, 'D':0} # 剩余玩家计数
        for p in senate: # 初始化游戏玩家数
            player_count[p] += 1

        # 待处刑玩家的阵营和数量
        target = None
        target_count = 0
        while q: # 开始回合
            # 检查获胜阵营
            if not player_count['R']:
                return 'Dire'
            if not player_count['D']:
                return 'Radiant'

            player = q.popleft() # 当前角色行动，只有队首的是当前玩家
            if target_count>0 and player==target: # 若当前玩家需要被杀死
                target_count -= 1
                player_count[player] -= 1
            else: # 若当前玩家可以行动
                target = 'R' if player=='D' else 'D' # 立即做出杀死后续对手的选择（只有杀死后面的对手才有意义，能避免其执行行动）
                target_count += 1 # 待处刑对手数量增加
                q.append(player) # 做出行动的玩家继续回到队尾等待它的下一轮行动

if __name__ == '__main__':
    senate = "RDDRRDDDRDRD"
    print(Solution().predictPartyVictory(senate))
