class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import sys
sys.path.insert(0,'../')
from problem.tree_node import MyTree

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        out = [-float('inf')]
        def dfs(node):#经过该节点的最大路径和（单分支）
            if node is None:
                return 0
            leftm = dfs(node.left)
            rightm = dfs(node.right)
            tmp = max(leftm+node.val,rightm+node.val,node.val)
            if max(tmp,leftm+rightm+node.val)>out[0]:
                out[0] = max(tmp,leftm+rightm+node.val)
            return tmp
        dfs(root)
        return out[0]

if __name__ == '__main__':
    pos = [5,-10,9,20,15,7]
    ins = [5,9,-10,15,20,7]
    root = MyTree.constuct_tree(pos,ins)
    so = Solution()
    print(so.maxPathSum(root))

