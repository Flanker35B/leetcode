'''
Lab8
Name: 35. Search Insert Position
https://leetcode.com/problems/search-insert-position/description/
'''


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0, len(nums)-1
        while l<= r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                l = mid +1
            else:
                r = mid - 1
        return l