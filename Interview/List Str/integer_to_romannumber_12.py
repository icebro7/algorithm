class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romannumber = {  
            1000: 'M',  
            900: 'CM',  
            500: 'D',  
            400: 'CD',  
            100: 'C',  
            90: 'XC',  
            50: 'L',  
            40: 'XL',  
            10: 'X',  
            9: 'IX',  
            5: 'V',  
            4: 'IV',  
            1: 'I'  
        }  
        res = ''
          
        # 按从大到小的顺序遍历罗马数字字符  
        for value, key in sorted(romannumber.items(), reverse=True):  # 抽取出key和value
            while num >= value:  # 将输入数与规定好的数字进行匹配，如大于等于则进入循环
                num -= value  # 将输入的数字减去规定好的数字
                res += key  # 把该罗马字符加入到res当中
        return res

if __name__ == '__main__':
    print(Solution().intToRoman(888))
    



