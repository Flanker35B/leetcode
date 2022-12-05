'''
Lab9
Name: 278. First Bad Version
https://leetcode.com/problems/first-bad-version/
'''


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1;
        begin = 1
        end = n
        while begin < end:
            mid = begin + (end - begin) / 2
            if isBadVersion(mid):
                end = mid
            else:
                begin = mid + 1
        return int(begin)
