def reverse_linkedlist(head):
    if head is None or head.next is None:
        return head
    
    prev = None
    curr = head
    next = None

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev

print(reverse_linkedlist([1,2,3,4,5]))