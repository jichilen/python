from tree_node import MyTree,MyTreeNode

def sym_tree(root):
    def sym_helper(node1,node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False
        return sym_helper(node1.left,node2.right) and sym_helper(node1.right,node2.left)
    if root is None:
        return True
    return sym_helper(root.left,root.right)

if __name__ == '__main__':
    pre = [8,6,5,7,6,7,5]
    inter = [5,6,7,8,7,6,5]
    root = MyTree.constuct_tree(pre,inter)
    MyTree.printtree(root)
    print(sym_tree(root))
