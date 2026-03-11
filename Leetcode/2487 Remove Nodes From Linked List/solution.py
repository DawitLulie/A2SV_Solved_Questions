# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prev = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        return prev
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        head = self.reverse(head)
        cur = head
        nxt = head.next


        while nxt:
            while nxt and nxt.val < cur.val:
                nxt = nxt.next

            cur.next = nxt
            cur = cur.next
            if nxt:
              nxt = nxt.next

        return self.reverse(head)

        