class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head or not head.next:
            return
        
        # Find the middle of the list
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Split the list into two halves
        secondHead = slow.next
        slow.next = None
        
        # Reverse the second half
        prev = None
        curr = secondHead
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        secondHead = prev  # This is now the head of the reversed second half
        
        # Merge the two halves
        first, second = head, secondHead
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
            
        return head




        
        