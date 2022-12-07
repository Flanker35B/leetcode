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
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd_head = ListNode()
        odd = odd_head
        even_head = ListNode()
        even = even_head
        count = 0
        while (head):
            if count % 2 == 0:
                odd.next = head
                odd = head
            else:
                even.next = head
                even = head
            count += 1
            head = head.next
        even.next = None
        odd.next = even_head.next      
        return odd_head.next
