'''
Lab2
Name: 203. Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int):
        new =ListNode() 
        new.next=head
        res=new
        while head:
            if head.val!=val:
                new=head
            else :
                new.next=head.next
            head=head.next
        return res.next