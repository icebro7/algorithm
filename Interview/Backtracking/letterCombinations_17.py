# @Time :2024/8/12 10:54
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtrack(index : int,path : List[str]):
            if index == len(digits):
                combinations.append("".join(path))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    path.append(letter)
                    backtrack(index + 1,path)
                    path.pop()

        combinations = []
        backtrack(0,[])
        return combinations
