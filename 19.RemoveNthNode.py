# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next == None:
            return None
        num = 0
        temp = head
        while temp.next != None:
            num += 1
            temp = temp.next
        if num < n:
            return head.next
        count = 0
        temp = head
        while count < num - n:
            count += 1
            temp = temp.next
        temp.next = temp.next.next
        return head
