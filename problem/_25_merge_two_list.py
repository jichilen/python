from list_node import My_ListNode,My_Linked_List

def merge_two_list(head1,head2):
    head = My_ListNode(0)
    tmp = head
    p1 = head1
    p2 = head2
    while p1 and p2:
        # 处理输入同一个链表（或者通一个链表的不同节点
        if p1 == p2:
            return head.next
        if p1.val<p2.val:
            tmp.next = p1
            p1 = p1.next
            tmp = tmp.next
        else:
            tmp.next = p2
            p2 = p2.next
            tmp = tmp.next
    if p2:
        p1,p2 = p2,p1
    tmp.next = p1
    return head.next



if __name__ == '__main__':
    head1 = My_Linked_List.linklist(list(range(1,10,2)))
    head2 = My_Linked_List.linklist(list(range(2,11,2)))
    My_Linked_List.printlist(head1)
    My_Linked_List.printlist(head2)
    head = merge_two_list(head1,head2)
    My_Linked_List.printlist(head)
    head1 = My_Linked_List.linklist(list(range(1, 10, 2)))
    head2 = My_Linked_List.linklist(list(range(2, 11, 2)))
    head = merge_two_list(head1, None)
    My_Linked_List.printlist(head)
    head1 = My_Linked_List.linklist(list(range(1, 10, 2)))
    head2 = My_Linked_List.linklist(list(range(2, 11, 2)))
    head = merge_two_list(None, head2)
    My_Linked_List.printlist(head)
    head1 = My_Linked_List.linklist(list(range(1, 3, 2)))
    head2 = My_Linked_List.linklist(list(range(2, 4, 2)))
    My_Linked_List.printlist(head1)
    My_Linked_List.printlist(head2)
    head = merge_two_list(head1, head2)
    My_Linked_List.printlist(head)
    head = merge_two_list(None, None)
    My_Linked_List.printlist(head)