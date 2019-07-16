from tree_node import MyTree
from collections import deque
def depth_of_tree(root):
    expanding = deque([root])
    n_expanding = deque()
    expanded = []
    d = 0
    while len(expanding)>0 or len(n_expanding)>0:
        while len(expanding)>0:
            node = expanding.popleft()
            expanded.append(node)
            if node.left:
                n_expanding.append(node.left)
            if node.right:
                n_expanding.append(node.right)
        expanding,n_expanding=n_expanding,expanding
        d += 1
    return d

def depth_of_tree1(root):
    def helper(node,k):
        if node is None:
            return k
        k += 1
        l = helper(node.left,k)
        r = helper(node.right,k)
        return max(l,r)
    return helper(root,0)

def ave_or_not(root):
    out = []
    def helper(node,k):
        if node is None:
            out.append(k)
            return k
        k += 1
        l = helper(node.left,k)
        r = helper(node.right,k)
        return max(l,r)
    helper(root,0)
    return out

if __name__ == '__main__':
    pre = [1,2,4,6,7,5,3]
    inter = [7,6,4,2,5,1,3]
    root = MyTree.constuct_tree(pre,inter)
    MyTree.printtree(root)
    # for _ in range(10000):
    #     depth_of_tree(root)
    #     depth_of_tree1(root)
    print(ave_or_not(root))