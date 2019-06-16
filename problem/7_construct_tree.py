class TreeNode():
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left= left
        self.right = right

def printpre(head):
    out = []
    def dfs(node):
        if node == None:
            return None
        out.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(head)
    print(out)

def printinter(head):
    out = []

    def dfs(node):
        if node == None:
            return
        dfs(node.left)
        out.append(node.val)
        dfs(node.right)
    dfs(head)
    print(out)

def printpos(head):
    out = []
    def dfs(node):
        if node == None:
            return
        dfs(node.left)
        dfs(node.right)
        out.append(node.val)
    dfs(head)
    print(out)

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
    printpre(pre)
    printinter(pre)
    printpos(pre)
    presub = [1,2,4,7,3,5,6,8]
    insub = [4,7,2,1,5,3,8,6]