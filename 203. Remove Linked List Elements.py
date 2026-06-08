class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    if not head:
        return None
    head.next = removeElements(head.next, val)
    return head.next if head.val == val else head
