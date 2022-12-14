'''
Name: 128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        cur, mx, cur_i= 0, 0, 0
        for i in nums:
            if i-1 not in nums:
                cur_i=i
                cur=1
            while cur_i+1 in nums:
                cur_i+=1
                cur+=1
            mx=max(mx,cur)
        return mx
