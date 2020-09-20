class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # hash 时间复杂度 O(N)，空间复杂度 O(N)
        cache = {k: 0 for k in arr2}
        others = []
        for i in arr1:
            if i not in cache:
                others.append(i)
            else:
                cache[i] += 1
        ans = []
        for i in arr2:
            ans.extend([i] * cache[i])
        ans.extend(sorted(others))
        return ans
