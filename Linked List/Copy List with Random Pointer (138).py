class Solution(object):
    def copyRandomList(self, head):
        old = {None : None}

        current = head
        while current:
            copy = Node(current.val)
            old[current] = copy
            current = current.next
        
        current = head
        while current:
            copy = old[current]
            copy.next = old[current.next]
            copy.random = old[current.random]
            current = current.next
        
        return old[head]