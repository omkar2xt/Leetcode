class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        ans = head
        carry = 0

        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            total = a + b + carry
            carry = total // 10

            ans.next = ListNode(total % 10)
            ans = ans.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            ans.next = ListNode(carry)

        return head.next