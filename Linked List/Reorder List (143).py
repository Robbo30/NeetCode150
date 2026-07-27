class Solution(object):
    def reorderList(self, head):
        # O(n) BRUTE FORCE 
        #
        # nodes = []
        # current = head
        # while current:
        #     nodes.append(current)
        #     current = current.next
        
        # left = 0
        # right = len(nodes) - 1
        # while left < right:
        #     nodes[left].next = nodes[right]
        #     left += 1
        #     nodes[right].next = nodes[left]
        #     right -= 1
        
        # nodes[left].next = None


        # O(n) REAL SOLUTION
        if not head or not head.next:
            return

        slow = head # use Hare-Tortoise algorithm to get middle of the list
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next # fast will be at the end whilst slow at the middle point so we can now access the 2nd half only

        second = slow.next
        slow.next = None # removes link between 1st and 2nd half
        previous = None

        while second: # then reverse the end half of the list 
            temp = second.next
            second.next = previous
            previous = second
            second = temp
        
        first = head
        second = previous

        while second: # then merge the 1st and 2nd lists together
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2