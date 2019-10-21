# Definition for a binary tree node.
import sys
sys.path.insert(0,'../')
from problem.tree_node import MyTree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        tmp = TreeNode(-9999)
        tmp.right = root
        root = tmp
        out = root
        l = 1
        while root is not None and root.val != key:
            lastr = root
            if root.val > key:
                root = root.left
                l = 1
            elif root.val < key:
                root = root.right
                l = 0
        if root is None:
            return out.right
        left = root.left
        right = root.right
        if l:
            p = 'left'
        else:
            p = 'right'
        if left is None:
            setattr(lastr, p, right)
        elif right is None:
            setattr(lastr, p, left)
        else:
            setattr(lastr, p, left)
            while left.right is not None:
                left = left.right
            left.right = right
        return out.right


def partition(nums,bg,ed):
    tmp = nums[bg]
    ti = bg+1
    for i in range(bg+1,ed):
        if nums[i]<tmp:
            nums[i],nums[ti] = nums[ti],nums[i]
            ti+=1
    ti-=1
    nums[bg],nums[ti] = nums[ti],nums[bg]
    return ti

def quicksort(nums,bg,ed):
    if bg>=ed:
        return
    mid = partition(nums,bg,ed)
    quicksort(nums,bg,mid)
    quicksort(nums,mid+1,ed)


def heapsort(nums):
    '''
    构建堆，交换构建堆
    :param nums:
    :return:
    '''
    ln = len(nums)
    for i in range((ln-1) // 2, -1, -1):
        heap_swap(nums, i, ln)
    for l in range(ln - 1, -1, -1):
        nums[l], nums[0] = nums[0], nums[l]
        heap_swap(nums, 0, l)


def heap_swap(nums, k, l):
    tmp = nums[k]
    while 2 * k + 1 < l:
        p = 2 * k + 1
        if p+1<l and nums[p]<nums[p+1]:
            p += 1
        if tmp < nums[p]:
            nums[k] = nums[p]
            k = p
        else:
            break
    nums[k] = tmp

if __name__ == '__main__':
    pos = [1,0,2]
    ins = [0,1,2]
    root = MyTree.constuct_tree(pos,ins)
    so = Solution()
    print(MyTree.printtree(so.deleteNode(root,1)))
    nums = [4,5,3,1]
    heapsort(nums)
    print(nums)
