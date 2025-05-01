# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            sumValue = carry
            if l1:
                sumValue += l1.val
                l1 = l1.next
            if l2:
                sumValue += l2.val
                l2 = l2.next
            carry = sumValue // 10
            current.next = ListNode(sumValue % 10)
            current = current.next
        return dummy.next
        