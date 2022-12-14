'''
Name:49. Group Anagrams
https://leetcode.com/problems/group-anagrams/
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for item in strs:
            if str(sorted(item)) in res:
                res[str(sorted(item))].append(item)
            else:
                res[str(sorted(item))] = [item]
                
        return list(res.values())
