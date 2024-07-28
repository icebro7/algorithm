# @Time :2024/7/10 8:58


class Solution:
    def simplifyPath(self, path: str) -> str:
        names = path.split("/")
        stack = list()

        for name in names:
            if name == "..":
                if stack:
                    stack.pop()
            elif name and name != ".":
                stack.append(name)

        return "/" + "/".join(stack)



if __name__ == '__main__':
    path = "../home/demo"

    result = Solution().simplifyPath(path)
    print(result)

