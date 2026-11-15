# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        arr = []
        res = ListNode()
        for lst in lists:
            while lst:
                arr.append(lst.val)
                lst = lst.next

        head = res
        arr.sort()
        for num in arr:
            head.next = ListNode(num)
            head = head.next

        return res.next



        