# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        retHead = ListNode(0)
        retTail = retHead
        retTail.next = head
        while retTail != None:
            count = 0
            tempK = retTail
            while count < k and tempK.next != None:
                tempK = tempK.next
                count += 1
            if count < k:
                break
            temp1 = retTail.next
            temp2 = temp1.next
            temp1.next = tempK.next
            retTail.next = tempK
            retTail = temp1
            num = 1
            while num < k:
                temp3 = temp2.next
                temp2.next = temp1
                temp1 = temp2
                temp2 = temp3
                num += 1
        return retHead.next