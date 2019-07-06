from tree_node import MyTreeNode, MyTree


def sub_tree_structure(root, subroot):
    def dfs_sub(node,subnode):
        if node is None and subnode is None:
            return True
        if node is None:
            return False
        if subnode is None:
            return False
        return dfs_sub(node.left,subnode.left) or dfs_sub(node.right,subnode.right)

    def bfs(node,subroot):
        if node is None and subroot is None:
            return True
        if node is None:
            return False
        if subroot is None:
            return False
        if node.val == subroot.val:
            if dfs_sub(node,subroot):
                return True
        return bfs(node.left,subroot) or bfs(node.right,subroot)
    return bfs(root,subroot)

if __name__ == '__main__':
    pre = [10, 8, 9, 2, 4, 7, 7]
    ins = [9, 8, 4, 2, 7, 10, 7]
    root = MyTree.constuct_tree(pre, ins)
    root.val = 8
    MyTree.printtree(root)
    pre = [8, 9, 2]
    ins = [9, 8, 2]
    subroot = MyTree.constuct_tree(pre,ins)
    print(sub_tree_structure(root,subroot))
    pre = [8, 9, 3]
    ins = [9, 8, 3]
    subroot = MyTree.constuct_tree(pre, ins)
    print(sub_tree_structure(root, subroot))
    print(sub_tree_structure(root, None))
    pre = [8,9,2,4,7]
    ins = [9,8,4,2,7]
    subroot = MyTree.constuct_tree(pre, ins)
    print(sub_tree_structure(root, subroot))

