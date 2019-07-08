class Complex_link_list():
    def __init__(self,val):
        self.val = val
        self.next = None
        self.sibling = None

    @classmethod
    def linklist(cls, nums):
        '''
        python 的list自带栈的功能
        :param nums:
        :return:
        '''
        head = Complex_link_list(nums[0])
        out = head
        for n in nums[1:]:
            head.next = Complex_link_list(n)
            head = head.next
        return out

    @classmethod
    def printlist_new(self, head):
        out = []
        outsib = []
        outnode = []
        while (head is not None):
            if head.sibling:
                outsib.append(head.sibling.val)
            else:
                outsib.append(None)
            out.append(head.val)
            outnode.append(head)
            head = head.next
        print(out)
        print(outsib)
        return outnode


def link_list_copy(head):
    #first double the link_list
    if head is None:
        return None
    node = head
    while node:
        nodecp = Complex_link_list(node.val)
        tmp = node.next
        node.next = nodecp
        nodecp.next = tmp
        node = node.next.next
    node = head
    out = head.next
    while node:
        if node.sibling:
            node.next.sibling = node.sibling.next
        node = node.next.next
        if out.next:
            out.next = out.next.next
        out = out.next
    return head.next


if __name__ == '__main__':
    head = Complex_link_list.linklist(range(5))
    outnode = Complex_link_list.printlist_new(head)
    outnode[0].sibling = outnode[2]
    outnode[1].sibling = outnode[4]
    outnode[2].sibling = None
    outnode[3].sibling = outnode[1]
    outnode[4].sibling = None
    print(id(head),head.val)
    Complex_link_list.printlist_new(head)
    node = link_list_copy(head)
    print(id(node),node.val)
    Complex_link_list.printlist_new(node)