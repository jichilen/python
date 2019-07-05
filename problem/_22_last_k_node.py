from list_node import My_ListNode,My_Linked_List

def last_k_node(head,k):
    p_slow=head
    p_fast=head
    if k<=0:
        return None
    for i in range(k):
        if p_fast is None:
            return None
        p_fast=p_fast.next
    while p_fast:
        p_fast=p_fast.next
        p_slow=p_slow.next
    return p_slow.val




if __name__ == '__main__':
    head = My_Linked_List.linklist(list(range(10)))

    print(last_k_node(head,2))
    print(last_k_node(head,4))
    print(last_k_node(head,6))
    print(last_k_node(head,8))
    print(last_k_node(head,10))
    print(last_k_node(head,12))
    print(last_k_node(head, 0))
    print(last_k_node(head, -1))