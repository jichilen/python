#前序：根左右
#中序：左根右
#后序：左右根

class MyTreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MyParent_TreeNode():
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        left = self.left.val if self.left is not None else 'None'
        right = self.right.val if self.right is not None else 'None'
        parent = self.parent.val if self.parent is not None else 'None'
        out = [self.val, left, right, parent]
        return ' '.join(out)


class MyTree():
    def __init__(self, pre, ins):
        self.head = self.constuct_tree(pre, ins)

    @classmethod
    def printtree(cls, head):
        outpre = []
        outinter = []
        outpos = []

        def dfs(node):
            if node == None:
                return None
            outpre.append(node.val)
            dfs(node.left)
            outinter.append(node.val)
            dfs(node.right)
            outpos.append(node.val)

        dfs(head)
        print(outpre)
        print(outinter)
        print(outpos)

    @classmethod
    def constuct_tree(cls, pre, ins):
        def iterfun(pre, ins):
            if len(pre) == 0:
                return None
            head = MyTreeNode(pre[0])
            cal = 0
            ro = pre[0]
            for i in ins:
                if i == ro:
                    break
                cal += 1
            head.left = iterfun(pre[1:cal + 1], ins[:cal])
            head.right = iterfun(pre[cal + 1:], ins[cal + 1:])
            return head

        if len(pre) == 0 or len(pre) != len(ins):
            return None
        return iterfun(pre, ins)
