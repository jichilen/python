from tree_node import MyTree

def tree_to_listnode(root):
    def helper(node):
        outl = node
        outr = node
        if node is None:
            return None,None
        l_left,l_right = helper(node.left)
        node.left = l_right
        if l_right:
            l_right.right = node
        if l_left:
            outl = l_left
        r_left,r_right = helper(node.right)
        if r_left:
            node.right = r_left
            r_left.left = node
        if r_right:
            outr = r_right
        return outl,outr
    return helper(root)

if __name__ == '__main__':
    pos = [10,6,4,8,14,12,16]
    inter = [4,6,8,10,12,14,16]
    root = MyTree.constuct_tree(pos,inter)
    MyTree.printtree(root)
    out = tree_to_listnode(root)