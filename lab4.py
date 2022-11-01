'''
Lab4
Name: 328. Odd Even Linked List
https://leetcode.com/problems/odd-even-linked-list/
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd=ListNode()
        even=ListNode()
        lh=0
        fh=head
        res=odd
        pr=even
        while fh:
            lh+=1
            fh=fh.next
        fh=head
        if lh%2==0:
            for i in range(lh//2):
                odd.next=fh
                odd=fh
                fh=fh.next
                even.next=fh
                even=fh
                fh=fh.next
        else:
            for i in range(lh//2):
                odd.next=fh
                odd=fh
                fh=fh.next
                even.next=fh
                even=fh
                fh=fh.next
            odd.next=fh
            odd=fh
        even.next=None
        odd.next=pr.next
        return res.next