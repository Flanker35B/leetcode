'''
Lab5
Name: 2181. Merge Nodes in Between Zeros
https://leetcode.com/problems/merge-nodes-in-between-zeros/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode()
        rf=res
        s=0
        head=head.next
        while head:
            if head.val!=0:
                s+=head.val
            else:
                res.next=head
                res=head
                res.val=s
                s=0
            head=head.next
        res.next=None
        return rf.next
