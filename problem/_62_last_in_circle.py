from list_node import My_Linked_List
def last_in_circle(n,k):
    head = My_Linked_List.linklist(range(n))
    tmp = head
    while tmp.next:
        tmp=tmp.next
    tmp.next=head
    while head.next is not head:
        for i in range(k-2):
            head = head.next
        head.next = head.next.next
        head= head.next
    return head.val

def last_in_circle1(n,k):
    #0,1,...,k-2,k,...,n-1
    #k,...n-1, 0,  1,...,k-2
    #0,...,   n-k, ...   n-2
    #x+k mod n
    out = 0
    for i in range(2,n+1):
        out = (out+k)%i
    return out

if __name__ == '__main__':
    print(last_in_circle(5,3))
    print(last_in_circle1(5,3))

