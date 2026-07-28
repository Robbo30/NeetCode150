class Solution(object):
    def removeNthFromEnd(self, head, n):
        # O(n) BRUTE FORCE
        #
        # nodes = []
        # current = head

        # while current:
        #     nodes.append(current)
        #     current = current.next
        
        # target = len(nodes) - n
        # if target == 0:
        #     return head.next
        
        # nodes[target - 1].next = nodes[target].next 
        # return head



        # O(n) REAL SOLUTION
        dummy = ListNode(0, head) # dummy node sitting before the head
        left = dummy
        right = head

        while n > 0: # move right pointer forward n times so right is n steps ahead of left
            right = right.next
            n -= 1

        while right: # move both pointers forward until right becomes None. As the gap was n, the moment right becomes None, the left pointer is on the node before the target.
            right = right.next
            left = left.next
        
        left.next = left.next.next # so drop the target
        return dummy.next