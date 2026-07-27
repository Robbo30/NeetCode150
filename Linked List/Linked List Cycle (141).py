class Solution(object): # Hare-Tortoise Algorithm
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next: # as long as fast can safely go forward
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                return True
        
        return False