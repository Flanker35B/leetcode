'''
Naame: 18. 4Sum
https://leetcode.com/problems/4sum/
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        if nums is None or len(nums) < 4:
            return ()
        
        set_a = set()
        res = set()
        
        for i in range(len(nums)):
            if nums[i] not in set_a:
                set_a.add(nums[i])
                for j in range(i+1, len(nums)):
                    dict = {}
                    for k in range(j+1, len(nums)):
                        a = nums[i]
                        b = nums[j]
                        c = nums[k]
                        d = target - a - b - c
                        if d not in dict:
                            dict[c] = k
                        else:
                            res.add(tuple(sorted([a,b,c,d])))
        return res
