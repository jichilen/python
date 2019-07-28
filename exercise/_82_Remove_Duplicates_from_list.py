# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:return
        tmp = ListNode(99999)
        tmp.next = head
        p1 = tmp
        p2 = tmp
        while p1.next.next:
            if p1.val != p1.next.val and p1.next.val != p1.next.next.val:
                p2.next = p1.next
                p2 = p2.next
            p1 = p1.next
        if p1.val == p1.next.val:
            p2.next = None
        else:
            p2.next = p1.next
        return tmp.next





if __name__ == '__main__':
    so = Solution()
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(2)
    print(so.deleteDuplicates(head).val)