'''
Lab12
Name: 1539. Kth Missing Positive Number
https://leetcode.com/problems/kth-missing-positive-number/
'''

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        res =0
        left,right=0, len(arr)
        while left<right:
            mid=left+(right-left)//2
            if arr[mid]-mid-1>=k:
                right=mid
            else:
                left=mid+1
        res=left+k
        return res
