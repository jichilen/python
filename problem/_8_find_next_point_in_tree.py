from _7_construct_tree import printtree

class TreeNode():
    def __init__(self,val,left=None,right=None,parent=None):
        self.val = val
        self.left= left
        self.right = right
        self.parent = parent
    def __repr__(self):
        left = self.left.val if self.left is not None else 'None'
        right = self.right.val if self.right is not None else 'None'
        parent = self.parent.val if self.parent is not None else 'None'
        out = [self.val,left,right,parent]
        return ' '.join(out)

def constuct_tree(pre,ins):
    def iterfun(pre,ins):
        if len(pre) == 0:
            return None
        head = TreeNode(pre[0])
        cal = 0
        ro = pre[0]
        for i in ins:
            if i == ro:
                break
            cal += 1
        head.left = iterfun(pre[1:cal+1],ins[:cal])
        head.right = iterfun(pre[cal + 1:], ins[cal+1:])
        if head.left is not None:
            head.left.parent = head
        if head.right is not None:
            head.right.parent = head
        return head
    if len(pre)==0 or len(pre)!= len(ins):
        return None
    return iterfun(pre,ins)

def find_next_point(head):
    if head is None:
        return None
    if head.right is not None:
        sn = head.right
        while sn.left is not None:
            sn = sn.left
        return sn
    elif head.parent is None:
        return None
    elif head.right is None and head.parent.left == head:
        return head.parent
    elif head.right is None and head.parent.right == head:
        sn = head
        while(sn.parent.right == sn):
            sn = sn.parent
            if sn.parent == None:
                return None
        return sn.parent.right
    return None



if __name__ == '__main__':
    presub = 'abdehicfg'
    presub = [i for i in presub]
    insub = 'd,b,h,e,i,a,f,c,g'.split(',')
    h = constuct_tree(presub, insub)
    printtree(h)
    n = find_next_point(h.left.right.right)
    print(n)
    n = find_next_point(h.left)
    print(n)