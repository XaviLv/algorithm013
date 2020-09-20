
class Solution:
    def reverseBits(self, n: int) -> int:
        """必须用位运算求解，转字符串做法得 0 分"""
        ans = 0
        for i in range(32):
            ans |= (n & 1) << (31 - i)
            n = n >> 1
        return ans