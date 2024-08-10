from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(course, adjacency, flags):
            if flags[course] == -1:  # 该节点已被访问过且无环
                return True
            if flags[course] == 1:  # 该节点正在被访问，说明有环
                return False

            flags[course] = 1  # 标记该节点正在被访问
            for next_course in adjacency[course]:
                if not dfs(next_course, adjacency, flags):
                    return False

            flags[course] = -1  # 该节点及其所有后代节点都无环
            return True

        adjacency = [set() for _ in range(numCourses)]
        flags = [0] * numCourses

        for cur, pre in prerequisites:
            adjacency[pre].add(cur)

        for course in range(numCourses):
            if not dfs(course, adjacency, flags):
                return False

        return True