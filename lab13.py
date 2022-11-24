'''
Lab13
Name: 912. Sort an Array
https://leetcode.com/problems/sort-an-array/
'''


class Solution: ##сортировка слиянием
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        left = self.sortArray(nums[:len(nums) // 2])
        right = self.sortArray(nums[len(nums) // 2:])
        i, j, x = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[x] = left[i]
                i = i + 1
            else:
                nums[x] = right[j]
                j = j + 1
            x = x + 1
        while i < len(left):
            nums[x] = left[i]
            x = x + 1
            i = i + 1
        while j < len(right):
            nums[x] = right[j]
            x = x + 1
            j = j + 1
            return nums

class Solution(object): ## быстрая сортировка
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)<=1:
            return nums
        else:
            mid=nums[len(nums)//2]
            left=[]
            cen=[]
            right=[]
            left = list(filter(lambda x: x<mid, nums))
            cen = [mid] * nums.count(mid)
            right =  list(filter(lambda x: x>mid, nums))
            return self.sortArray(left) + cen + self.sortArray(right)