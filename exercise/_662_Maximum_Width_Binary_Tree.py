# Definition for a binary tree node.
import sys

sys.path.insert(0, '../')
from tree_node import MyTree
from tree_node import MyTreeNode as TreeNode
from collections import deque


class Solution:
    def widthOfBinaryTree(self, head: TreeNode) -> int:
        expanding = deque()
        maxw = 0
        if head is None:
            return 0
        expanding.append([head, 0])
        while len(expanding) > 0:
            l = len(expanding)
            maxw = max(maxw, expanding[-1][1] - expanding[0][1] + 1)
            for i in range(l):
                node, val = expanding.popleft()
                if node.left is not None:
                    expanding.append([node.left, val * 2])
                if node.right is not None:
                    expanding.append([node.right, val * 2 + 1])
        return maxw


if __name__ == '__main__':
    so = Solution()
    pos = [1, 3, 5, 6, 2, 9, 7]
    inter = [6, 5, 3, 1, 2, 9, 7]
    head = MyTree.constuct_tree(pos, inter)
    print(so.widthOfBinaryTree(head))
