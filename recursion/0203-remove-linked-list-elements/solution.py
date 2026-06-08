class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        res = []
        curr = self
        while curr:
            res.append(str(curr.val))
            curr = curr.next
        return " -> ".join(res)

def removeElements(head, val):
    if not head:
        return None
    head.next = removeElements(head.next, val)
    return head.next if head.val == val else head

# Test code
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    print("Original List:", head)
    print("Modified List (remove 6):", removeElements(head, 6))
