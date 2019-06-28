from list_node import My_Linked_List,My_ListNode
def del_node(head,n):
    if n < 0:
        return head
    if n == 0:
        return head.next
    tmp = head
    for i in range(n-1):
        if tmp.next is not None:
            tmp = tmp.next
        else:
            return None
    if tmp.next:
        # if tmp.next.next:
        #     tmp.next =tmp.next.next
        # else:
        #     tmp.next = None
        tmp.next = tmp.next.next
        return head
    return head

def del_dum_node(head):
    num = 0
    if head.val == num:
        num +=1
    tmp = My_ListNode(num,head)
    head = tmp
    My_Linked_List.printlist(tmp)
    while tmp.next:
        p = tmp
        while p.next.next:
            if p.next.val != p.val and p.next.next.val != p.next.val:
                break
            p = p.next
        if not p.next.next:
            tmp.next = None
            break
        else:
            tmp.next = p.next
        tmp = tmp.next

    return head.next

if __name__ == '__main__':
    for n in range(-1,9):
        head = My_Linked_List.linklist([1, 5, 4, 2, 3, 11, 2, 3])
        out = del_node(head,n)
        My_Linked_List.printlist(out)
    print()
    head = My_Linked_List.linklist([1,1,2,3,4,4,5,6,6])
    out = del_dum_node(head)
    My_Linked_List.printlist(out)