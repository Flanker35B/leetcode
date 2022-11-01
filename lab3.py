'''
Lab3
Name: 160. Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) :
        fa=headA
        fb=headB
        la=lb=0
        while fa:
            la+=1
            fa=fa.next
        while fb:
            lb+=1
            fb=fb.next
        fa=headA
        fb=headB
        if la>lb:
            for i in range(la-lb):
                fa=fa.next
        if la<lb:
            for i in range(lb-la):
                fb=fb.next
        while fa!=fb:
            fa=fa.next
            fb=fb.next
        return fa