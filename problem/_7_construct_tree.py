class TreeNode():
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left= left
        self.right = right

def printtree(head):
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
        return head
    if len(pre)==0 or len(pre)!= len(ins):
        return None
    return iterfun(pre,ins)

if __name__ == '__main__':
    pre = TreeNode(10)
    pre.left = TreeNode(6)
    pre.right = TreeNode(14)
    pre.left.left = TreeNode(4)
    pre.left.right = TreeNode(8)
    pre.right.left = TreeNode(12)
    pre.right.right = TreeNode(16)
    printtree(pre)
    presub = [1,2,4,7,3,5,6,8]
    insub = [4,7,2,1,5,3,8,6]
    h = constuct_tree(presub,insub)
    printtree(h)