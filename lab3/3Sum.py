'''
Name: 15. 3Sum
https://leetcode.com/problems/3sum/description/
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i, a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                curSum= a + nums[l]+nums[r]
                if curSum> 0:
                    r-=1
                elif curSum<0:
                    l+=1
                else:
                    res.add((a, nums[l] ,nums[r]))
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res
