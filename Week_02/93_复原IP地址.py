#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        COUNT = 4
        segments, ans = [0]*COUNT, []
        
        def dfs(sid, start):
            # 终止条件
            if sid == COUNT and start == len(s):
                ipaddr = '.'.join([str(m) for m in segments])
                ans.append(ipaddr)
                return
            if sid == COUNT or start == len(s):
                return
            # 搜索过程
            if s[start] == '0': # 除数字0外，不能以0开头，注意这里适合字符'0'比较
                segments[sid] = s[start]
                dfs(sid+1, start+1)
                return
            num = 0
            for i in range(start, len(s)):
                num = num * 10 + int(s[i])
                if 255 >= num > 0:
                    segments[sid] = num
                    dfs(sid+1, i+1)
                else:
                    break
        dfs(0, 0)
        return ans
        
# @lc code=end

