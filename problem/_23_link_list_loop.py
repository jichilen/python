from list_node import My_ListNode,My_Linked_List
def link_list_loop(head):
    if head is None:
        return None
    p_slow = head
    p_fast = head
    c1 = 0
    while c1==0 or p_slow != p_fast:
        c1 +=1
        if p_fast.next and p_fast.next.next:
            p_fast=p_fast.next.next
        else:
            # no loop
            return None
        p_slow = p_slow.next
    cout = 0
    while cout == 0 or p_slow != p_fast:
        p_fast=p_fast.next.next
        p_slow = p_slow.next
        cout += 1
    p_slow = head
    p_fast = head
    for _ in range(cout):
        p_fast=p_fast.next
    while p_slow!=p_fast:
        p_fast = p_fast.next
        p_slow = p_slow.next
    return cout,p_slow.val

if __name__ == '__main__':
    head = My_Linked_List.linklist(list(range(11)))
    tmp =head
    while tmp.next:
        tmp = tmp.next
    ttmp = head
    for _ in range(5):
        ttmp = ttmp.next
    tmp.next = ttmp
    print(link_list_loop(head))