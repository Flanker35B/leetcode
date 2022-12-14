'''
Name: 560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res, totalSum = 0, 0
        hashmap = {0:1}
        for i in nums:
            totalSum += i
            diff=totalSum-k
            if hashmap.get(diff):
                res += hashmap[diff]              
            if hashmap.get(totalSum):
                hashmap[totalSum] += 1
            else:
                hashmap[totalSum] = 1
        return res
