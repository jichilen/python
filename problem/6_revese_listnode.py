
class ListNode():
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def reverse_listnode(head):
    out = []
    while head != None :
        out.append(head.val)
        head=head.next
    while len(out)!=0:
        print(out.pop())


def linklist(nums):
    '''
    python 的list自带栈的功能
    :param nums:
    :return:
    '''
    head = ListNode(nums[0])
    out = head
    for n in nums[1:]:
        head.next = ListNode(n)
        head = head.next
    return out

def printlist(head):
    out = []
    while(head is not None):
        out.append(head.val)
        head = head.next
    print(out)

if __name__ == '__main__':
    list = [1,3,4,6,6,1]
    ll = linklist(list)
    printlist(ll)
    reverse_listnode(ll)