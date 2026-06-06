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

def mergesort(l1,l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.val < l2.val:
        l1.next = mergesort(l1.next,l2)
        return l1
    else:
        l2.next = mergesort(l1,l2.next)
        return l2

# Test code
if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    print("List 1:", l1)
    print("List 2:", l2)
    print("Merged List:", mergesort(l1, l2))
