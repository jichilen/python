from tree_node import MyTree

def tree_sum(root,target):
    def search(node,target,re):
        if node is None:
            return None
        val = re[0]+node.val
        if val>target:
            return None
        past = re[1].copy()
        past.append(node.val)
        if val==target:
            return [past]
        re_n = [val,past]
        left = search(node.left,target,re_n)
        right = search(node.right, target, re_n)
        out =[]
        if left:
            out.extend(left)
        if right:
            out.extend(right)
        return out
    re = [0,[]]
    return search(root,target,re)

if __name__ == '__main__':
    pos = [10,5,4,7,12]
    inter = [4,5,7,10,12]
    root = MyTree.constuct_tree(pos,inter)
    target = 22
    print(tree_sum(root,target))