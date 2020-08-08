#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: return []

        def way1():
            # sort 时间复杂度 O(K * NlogN)，空间复杂度 O(K); easy to recall
            mem = defaultdict(list)
            for word in strs:
                t = ''.join(sorted(word))
                mem[t].append(word)
            return [v for v in mem.values()]

        def way2():
            # array 时间复杂度 O(K * N), slow in string key construct 
            mem = defaultdict(list)
            ch_int = {chr(k): k for k in range(97, 123)}
            for word in strs:
                array = [0] * 26
                for c in word:
                    array[ch_int[c]-ch_int['a']] += 1
                key = '#'.join([str(m) for m in array])
                mem[key].append(word)
            return [v for v in mem.values()]

        def way3():
            # use prime to construct key; improved on way2
            primes = [2, 3, 5, 7, 11 ,13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
            ch_int = {chr(k): k for k in range(97, 123)}
            mem = defaultdict(list)
            for word in strs:
                key = 1
                for c in word:
                    key *= primes[ch_int[c] - ch_int['a']]
                mem[key].append(word)
            return [v for v in mem.values()]

        return way1()
# @lc code=end

