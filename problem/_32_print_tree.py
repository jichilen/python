from tree_node import MyTree,MyTreeNode
from collections import deque

def print_tree(root):
    if root is None:
        return
    expanding = deque()
    expanding.append(root)
    expanded = []
    while len(expanding)>0:
        node = expanding.popleft()
        if node:
            expanded.append(node.val)
            expanding.append(node.left)
            expanding.append(node.right)
    print(expanded)

def print_tree1(root):
    if root is None:
        return
    expanding = deque()
    expanding_next= deque()
    expanding.append(root)
    expanded = []
    depth = 0
    while len(expanding)>0:
        depth+=1
        while len(expanding) > 0:
            node = expanding.popleft()
            if node:
                expanded.append([node.val,depth])
                expanding_next.append(node.left)
                expanding_next.append(node.right)
        expanding,expanding_next = expanding_next,expanding
    print(expanded)


if __name__ == '__main__':
    pre= [8,6,5,7,10,9,11]
    inter = [5,6,7,8,9,10,11]
    root = MyTree.constuct_tree(pre,inter)
    MyTree.printtree(root)
    print_tree(root)
    print_tree1(root)
