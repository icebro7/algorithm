# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
# 解释：需要合并 [1,2,3] 和 [2,5,6] 。
# 合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 & n != 0:
            for x in range(n):
                nums1.append(nums2[x])
        elif m == 0 and n == 0:
            nums1 = [0]
        else:
            z = 0
            for i in range(m,(n+m)):
                nums1[i] = nums2[z]
                z += 1

            nums1.sort()


        return nums1
if __name__ == '__main__':
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1

    print(Solution().merge(nums1,m,nums2,n))
