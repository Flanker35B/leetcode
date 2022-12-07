'''
Lab14
Name: 268. Missing Number
https://leetcode.com/problems/missing-number/
'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        exp_sum = len(nums)*(len(nums)+1)//2
        act_sum = sum(nums)
        return exp_sum - act_sum
