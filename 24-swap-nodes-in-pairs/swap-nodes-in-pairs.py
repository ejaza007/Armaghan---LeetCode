# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            firstNode = head
            secNode = head.next

            prev.next = secNode
            firstNode.next = secNode.next
            secNode.next = firstNode

            prev = firstNode
            head  = firstNode.next
        return dummy.next


        
        