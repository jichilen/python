from tree_node import MyTree,MyTreeNode
from collections import deque
def serialize(root):
    out = []
    def helper(node):
        if node is None:
            out.append('$')
            return
        out.append(node.val)
        helper(node.left)
        helper(node.right)
    helper(root)
    return out

def deserialize(list):
    list = deque(list)
    def helper(list):
        tmp = list.popleft()
        if tmp != '$':
            node = MyTreeNode(tmp)
            node.left = helper(list)
            node.right = helper(list)
            return node
        return None
    return helper(list)

if __name__ == '__main__':
    pos = [1,2,4,3,5,6]
    inter = [4,2,1,5,3,6]
    root = MyTree.constuct_tree(pos,inter)
    MyTree.printtree(root)
    selist = serialize(root)
    node = deserialize(selist)
    MyTree.printtree(node)