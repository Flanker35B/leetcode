'''
Lab11
Name: 852. Peak Index in a Mountain Array
https://leetcode.com/problems/peak-index-in-a-mountain-array/
'''


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 1, len(arr)-1
        while l<=r:
            mid= (l+r)//2
            if arr[mid-1]>arr[mid]:
                r=mid-1
            else:
                l=mid+1
        return r
