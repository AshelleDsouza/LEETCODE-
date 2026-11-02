class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode(0)
        large = ListNode(0)

        p1 = small
        p2 = large

        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next

            head = head.next

        p2.next = None
        p1.next = large.next

        return small.next