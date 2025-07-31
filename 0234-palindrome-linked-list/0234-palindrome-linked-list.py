# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_val=[]
        curr=head
        while curr:
            list_val.append(curr.val)
            curr=curr.next
        if list_val==list_val[::-1]:
            return True
        return False