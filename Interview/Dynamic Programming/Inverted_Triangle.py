import timeit


class Main:
    def length_of_LIS(self,nums):
        n = len(nums)   
        L = [1] * n #创建一个具有这么大容量的一个列表   

        for i in reversed(range(n)):    #用i从nums的最后一位开始循环，即倒三角模式
            for j in range(i+1,n):  #从倒数的第i+1位开始到最后做循环
                if nums[j] > nums[i]:   #判断循环中第j个数到最后一个数里面，是否存在比第i个数更大的递增
                    L[i] = max(L[i],L[j] + 1)   #如有，则记录
        
        return  max(L)

def measure_execution_time():  
    main_instance = Main()  
    main_instance.length_of_LIS(nums)  
    
nums =[
    45, 78, 34, 67, 90, 15, 48, 72, 39, 61
]


if __name__ == '__main__':
    print(Main().length_of_LIS(nums))

    # execution_time = timeit.timeit(measure_execution_time, number=1)  
    # print(execution_time)
    

                
