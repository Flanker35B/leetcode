'''
Name: 1893. Check if All the Integers in a Range Are Covered
https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/
'''
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        sas={}
        for i in range (left, right+1):
            sas[i]=0
        
        for item in sas:
            for l, r in ranges:
                if l<=item<=r:
                    sas[item]=1
                    break
            if sas[item]==0:
                return False
        return True
