from _7_construct_tree import printtree

class TreeNode():
    def __init__(self,val,left=None,right=None,parent=None):
        self.val = val
        self.left= left
        self.right = right
        self.parent = parent

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
        head.left.parent = head
        head.right.parent = head
        return head
    if len(pre)==0 or len(pre)!= len(ins):
        return None
    return iterfun(pre,ins)

