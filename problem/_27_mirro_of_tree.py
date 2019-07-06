from tree_node import MyTree,MyTreeNode

def mirror_of_tree(root):
    def bfs(node):
        if node is None:
            return
        node.left,node.right = node.right,node.left
        bfs(node.left)
        bfs(node.right)
    bfs(root)

if __name__ == '__main__':
    pre = [8,6,5,7,10,9,11]
    inter = [5,6,7,8,9,10,11]
    root = MyTree.constuct_tree(pre,inter)
    MyTree.printtree(root)
    mirror_of_tree(root)
    MyTree.printtree(root)
    pre = [8, 6, 7, 10, 9, 11]
    inter = [6, 7, 8, 9, 10, 11]
    root = MyTree.constuct_tree(pre, inter)
    mirror_of_tree(root)
    MyTree.printtree(root)
