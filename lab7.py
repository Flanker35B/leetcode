'''
Lab7
Name: 2095. Delete the Middle Node of a Linked List
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fh=head
        lh=0
        while fh:
            lh+=1
            fh=fh.next
        if lh==1:
            return None
        elif lh==2:
            head.next=None
            return head
        else:
            fh=head
            for i in range(lh//2):
                head=head.next
            head.val=head.next.val
            head.next=head.next.next
        return fh