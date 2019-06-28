class My_ListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class My_Linked_List():
    def __init__(self, nums):
        self.head = self.linklist(nums)

    @classmethod
    def linklist(cls, nums):
        '''
        python 的list自带栈的功能
        :param nums:
        :return:
        '''
        head = My_ListNode(nums[0])
        out = head
        for n in nums[1:]:
            head.next = My_ListNode(n)
            head = head.next
        return out

    @classmethod
    def printlist(cls, head):
        out = []
        while (head is not None):
            out.append(head.val)
            head = head.next
        print(out)
