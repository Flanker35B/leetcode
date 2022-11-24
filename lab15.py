'''
Lab15
Name: 2418. Sort the People
https://leetcode.com/problems/sort-the-people/
'''


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
      return list(a for b,a in sorted (zip(heights,names),reverse=True))