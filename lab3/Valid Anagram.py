'''
Name: 242. Valid Anagram
https://leetcode.com/problems/valid-anagram/
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        sd= {}
        for i in s:
            if i not in sd:
                sd[i]=1
            else:
                sd[i]+=1
            
        for i in t:
            if i not in sd:
                return False
            else:
                sd[i]-=1
                if sd[i]<0:
                    return False
        return True
