class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            
            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            
            sum = val1 + val2 + carry
            carry = sum // 10
            digit = sum % 10

            current.next = ListNode(digit)
            current = current.next
        
        return dummy.next
            