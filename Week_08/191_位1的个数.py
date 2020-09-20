class Solution:
    def hammingWeight(self, n: int) -> int:
        # # way1: 位运算
        # i = 0
        # while n != 0:
        #     n = n & (n - 1) # 清零从右往左数第一个1
        #     i += 1
        # return i
        
        # way2: bin 函数
        return bin(n).count('1')