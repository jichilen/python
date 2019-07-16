from list_node import My_Linked_List
def cal_l(head):
    count = 1
    while head.next:
        head=head.next
        count+=1
    return count

def share_node_in_linklist(head1,head2):
    l1 = cal_l(head1)
    l2 = cal_l(head2)
    if l1>l2:
        head1,head2 = head2,head1
        l1,l2 = l2,l1
    #l1<=l2
    for _ in range(l2-l1):
        head2=head2.next
    while head1 is not head2:
        if head1.next:
            head1 = head1.next
            head2 = head2.next
        else:
            return None
    return head1



if __name__ == '__main__':
    head1 = My_Linked_List.linklist(range(10))
    tmp = head1
    for _ in range(4):
        tmp=tmp.next
    head2 = My_Linked_List.linklist([4,2,1,3,4])
    tmp2=head2
    while tmp2.next:
        tmp2 = tmp2.next
    tmp2.next = tmp.next
    My_Linked_List.printlist(head1)
    My_Linked_List.printlist(head2)
    print(share_node_in_linklist(head1,head2).val)