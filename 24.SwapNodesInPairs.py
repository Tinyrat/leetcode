# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        retHead = ListNode(0)
        retTail = retHead
        if head != None:
            retTail.next = head
        while retTail != None:
            if retTail.next == None or retTail.next.next == None:
                break
            temp = retTail.next
            retTail.next = retTail.next.next
            temp.next = retTail.next.next
            retTail.next.next = temp
            retTail = retTail.next.next
        return retHead.next
