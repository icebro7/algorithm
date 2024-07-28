from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L = len(nums)

        while val in nums:      #如果val在nums中的话那就把这个数从nums中移走
            nums.remove(val)        #remove和pop之间的区别：
                                    #remove会搜索到第一个匹配项，并且不返回任何内容
                                    #pop需要按照指定位置的索引（传递）搜索，返回元素的值

        return len(nums),nums



if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(Solution().removeElement(nums,val))
