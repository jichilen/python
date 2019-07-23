class MyListNode():
    def __init__(self,a):
        self.val = a
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.len = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if not isinstance(index,int):return -1
        if index<0:return -1
        if index>=self.len: return -1
        tmp = self.head
        for _ in range(index):
            if tmp.next:
                tmp = tmp.next
            else:
                return -1
        return tmp.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        tmp = self.head
        self.head = MyListNode(val)
        self.head.next = tmp
        self.len+=1
        if not self.tail:
            self.tail = self.head

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if not self.tail:
            return self.addAtHead()
        self.tail.next = MyListNode(val)
        self.tail = self.tail.next
        self.len+=1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index>self.len: return
        if index<=0: return self.addAtHead(val)
        if index==self.len: return self.addAtTail(val)
        tmp = self.head
        for _ in range(index-1):
            tmp = tmp.next
        ttmp = tmp.next
        tmp.next = MyListNode(val)
        tmp.next.next = ttmp
        self.len+=1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index<0:return
        if index>=self.len: return
        self.len-=1
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return
        tmp = self.head
        for _ in range(index-1):
            tmp=tmp.next
        tmp.next=tmp.next.next
        if tmp.next is None:
            self.tail = tmp

    def printl(self):
        tmp = self.head
        out = []
        while tmp is not None:
            out.append(tmp.val)
            tmp=tmp.next
        print(out,self.head.val if self.head else None,self.tail.val if self.tail else None)

# Your MyLinkedList object will be instantiated and called as such:
if __name__ == '__main__':
    a=["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
    b=[[], [1], [3], [4, 2], [1], [-1], [1]]
    obj = MyLinkedList()
    for fun,arg in zip(a[1:],b[1:]):
        getattr(obj,fun)(*arg)
        obj.printl()