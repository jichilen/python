from tree_node import MyTree


def kth_largest_in_tree(root, k):
    out = []
    def helper(node):
        if node is None:
            return
        helper(node.left)
        out.append(node.val)
        helper(node.right)
    helper(root)
    return out[-k]


if __name__ == '__main__':
    pre = [5,3,2,4,7,6,8]
    inter = [2,3,4,5,6,7,8]
    root = MyTree.constuct_tree(pre,inter)
    print(kth_largest_in_tree(root,4))
