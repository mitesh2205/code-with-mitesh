def sortList(head):
    if not head or head.next is None:
        return head
    slow, fast = head, head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = sortList(head)
    right = sortList(mid)

    return merge(left, right)

def merge(left, right):
    dummy = ListNode(0)
    curr = dummy

    while left and right:
        if left.val < right.val:
            curr.next= left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next

        left if left else right

    return dummy.next
