class Solution:
    def isValid(self, s):
        while '{}' in s or '()' in s or '[]' in s:  #直接配对括号，若存在则替换为空，不存在则return false
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''

class Solution2:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic: stack.append(c)
            elif dic[stack.pop()] != c: return False
        return len(stack) == 1


class Solution3:
    def isValid(self, s: str) -> bool:
        dic = {'’':'‘','”':'“','<':'>','?':'?'}
        stack = ['?']

        for i in s:
            if i in dic:
                stack.append(i)
            elif dic[stack.pop()] != i:
                return False
        return len(stack) == 1


if __name__ == '__main__':
    s = '’‘”<>“'
    print(Solution3().isValid(s=s))
