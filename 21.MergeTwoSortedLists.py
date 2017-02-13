# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        if l1.val < l2.val:
            head = l1
            temp = head
            l1 = l1.next
        else:
            head = l2
            temp = l2
            l2 = l2.next
        while l1 != None or l2 != None:
            if l1 == None:
                temp.next = l2
                break
            elif l2 == None:
                temp.next = l1
                break
            else:
                if l1.val < l2.val:
                    temp.next = l1
                    l1 = l1.next
                else:
                    temp.next = l2
                    l2 = l2.next
                temp = temp.next
        return head
