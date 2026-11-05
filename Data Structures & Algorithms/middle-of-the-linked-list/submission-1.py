# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # O(n/2)
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

        # O(n + n//2)
        res = head
        count = 0
        while head:
            count += 1
            head = head.next
        
        for i in range(count//2):
            res = res.next

        return res

