from list_node import My_ListNode,My_Linked_List
# 在链表操作室要注意链表之间的断开
# 尤其要注意第一个节点和最后一个节点的操作
def reverse_link_list(head):
    if head is None:
        return None
    if head.next is None:
        return head
    p_pre=head.next
    if head.next.next is None:
        p_pre.next = head
        head.next = None
        return p_pre
    p_next = head.next.next
    p_pre.next = head
    head.next = None
    while p_next.next:
        p_tmp = p_next
        p_next = p_next.next
        p_tmp.next = p_pre
        p_pre = p_tmp
    p_next.next = p_pre
    return p_next

def reverse(head):
    if head is None:
        return None
    p1 = head
    if p1.next:
        p2 = p1.next
    else:
        return head
    p1.next = None
    while p2.next:
        sa = p2.next
        p2.next = p1
        p1 = p2
        p2 = sa
    p2.next = p1
    return p2

def reverse2(head):
    def dfs(node):
        if node.next:
            re = dfs(node.next)
            re.next = node
        return node
    re = dfs(head)
    head.next = None
    return re

if __name__ == '__main__':
    head= My_Linked_List.linklist(list(range(10)))
    out = reverse_link_list(head)
    My_Linked_List.printlist(out)
    head= My_Linked_List.linklist(list(range(1)))
    out = reverse_link_list(head)
    My_Linked_List.printlist(out)
    head= My_Linked_List.linklist(list(range(2)))
    out = reverse_link_list(head)
    My_Linked_List.printlist(out)
    head = My_Linked_List.linklist(list(range(10)))
    out = reverse(head)
    My_Linked_List.printlist(out)
    head = My_Linked_List.linklist(list(range(10)))
    out = reverse2(head)
    My_Linked_List.printlist(out)
