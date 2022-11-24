'''
Lab12
Name: 1539. Kth Missing Positive Number
https://leetcode.com/problems/kth-missing-positive-number/
'''

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        mis=0
        i=1
        while mis!=k:
            if  i not in arr:
                mis+=1
            if mis==k:
                return i
            i+=1