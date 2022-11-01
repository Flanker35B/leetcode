'''
Lab6
Name: 237. Delete Node in a Linked List
https://leetcode.com/problems/delete-node-in-a-linked-list/
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        node.val=node.next.val
        node.next=node.next.next