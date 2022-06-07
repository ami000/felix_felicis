import math
import unittest

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# iterative
def treeMaxPathSumDftI (root: TreeNode):
    if root is None: return -math.inf
    stack = [root]
    maxSum = 0
    maxPathSum = -math.inf
    while len(stack) > 0:
        curr = stack.pop()
        if curr.data: maxSum += max(maxPathSum, curr.data)
        if curr.right: stack.append(curr.right)
        if curr.left: stack.append(curr.left)
    return maxSum

def treeMaxPathSumBftI (root: TreeNode):
    if root is None: return 0
    q = [root]
    lowest = math.inf
    while len(q) > 0:
        curr = q.pop(0)
        lowest = min(lowest, curr.data)
        if curr.left: q.append(curr.left)
        if curr.right: q.append(curr.right)
    return lowest

# recursive

def treeMaxPathSumDftR (root:TreeNode):
    if root is None: return -math.inf
    if root.left is None and root.right is None: return root.data
    return root.data + max(treeMaxPathSumDftR(root.left), treeMaxPathSumDftR(root.right))

def buildTree():
    a = TreeNode(3)
    b = TreeNode(11)
    c = TreeNode(4)
    d = TreeNode(4)
    e = TreeNode(-2)
    f = TreeNode(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    return a

class MyTestCase(unittest.TestCase):
    def test_something(self):
        root  = buildTree()
        # self.assertEqual(18, treeMaxPathSumDftI(root))  # add assertion here
        # self.assertEqual(18, treeMaxPathSumBftI(root))  # add assertion here
        self.assertEqual(18, treeMaxPathSumDftR(root))  # add assertion here
        # self.assertEqual(-math.inf, treeMaxPathSumDftR(None))


if __name__ == '__main__':
    unittest.main()
