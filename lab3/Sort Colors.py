'''
Name: 75. Sort Colors
https://leetcode.com/problems/sort-colors/
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        d={0:0,1:0,2:0}
        for i in nums:
            d[i]+=1
        for i in range(d[0]):
            nums[i]=0
        for i in range(d[0], d[0]+ d[1]):
            nums[i]=1
        for i in range( d[0]+ d[1],d[0]+ d[1]+ d[2]):
            nums[i]=2
