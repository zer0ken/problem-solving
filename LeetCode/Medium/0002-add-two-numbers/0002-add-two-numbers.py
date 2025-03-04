# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        l1_ = l1
        zero = ListNode(val=0)
        while True:
            t = l1.val + l2.val + c
            l1.val = t % 10
            c = t // 10

            if l1.next is None and l2.next is None:
                if c:
                    l1.next = ListNode(val=1)
                    break
                else:
                    break
            elif l1.next is None:
                if c:
                    l1.next = ListNode(val=c)
                    c = 0
                else:
                    l1.next = l2.next
                    break
            elif l2.next is None:
                if c:
                    l2.next = ListNode(val=c)
                    c = 0
                else:
                    break
            l1 = l1.next
            l2 = l2.next
        
        return l1_