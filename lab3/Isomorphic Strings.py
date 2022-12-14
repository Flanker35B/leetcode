'''
Name: 205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/
'''

class Solution:
    def isom(self,s: str, t: str ):
        dict={}
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]]=t[i]
            else:
                if dict[s[i]]!=t[i]:
                    return False
        return True

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        if self.isom(s,t)and self.isom(t,s):
            return True
        else: 
            return False
