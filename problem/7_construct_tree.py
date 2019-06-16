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
    pass



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