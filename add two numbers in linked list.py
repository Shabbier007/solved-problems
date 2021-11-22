def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    main = ListNode(0)
    prev = main
    x_carry = 0
    while True:
        if l1 is None and l2 is None and x_carry == 0:
            break
        if not l1 or l1 is None:
            a = 0
        else:
            a = l1.val
            l1 = l1.next
        if not l2 or l2 is None:
            b = 0
        else:
            b = l2.val
            l2 = l2.next
        temp = ListNode(0)
        total_sum = a + b
        carry_sum = total_sum + x_carry
        total_carry_sum = (total_sum % 10) + x_carry
        insert_val = total_carry_sum % 10
        temp.val = insert_val
        prev.next = temp
        prev = temp
        x_carry = carry_sum // 10
    return main.next
