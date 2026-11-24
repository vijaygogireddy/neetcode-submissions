# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find start of second half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next  # by visualization

        # reverse the second half -- reverse pointers
        slow.next = None # break link btw first and second half
        curr = None

        while second:
            temp = second.next
            second.next = curr
            curr = second
            second = temp

        # merge two halfs
        first, second = head, curr
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

