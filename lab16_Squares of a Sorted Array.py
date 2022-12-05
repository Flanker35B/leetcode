'''
Lab16
Name: 977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/
'''


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        L, R, res = 0, len(nums) - 1, []
        while L <= R:
            if abs(nums[L]) >= abs(nums[R]):
                res.append(nums[L] ** 2)
                L += 1
            else:
                res.append(nums[R] ** 2)
                R -= 1
        return res[::-1]
