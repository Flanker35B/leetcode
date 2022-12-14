'''
Name: 1. twoSum
https://leetcode.com/problems/two-sum/
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pmap={}

        for i, n in enumerate(nums):
            d= target - n
            if d in pmap:
                return [pmap[d], i]
            pmap[n]=i
