import unittest

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# iterative
def dfsI (root: TreeNode, target):
    if root is None: return False
    stack = [root]
    while len(stack) > 0:
        curr = stack.pop()
        if curr.data == target: return True
        if curr.right: stack.append(curr.right)
        if curr.left: stack.append(curr.left)
    return False

# recursive

def dfsR (root:TreeNode, target):
    if root is None: return False
    if root.data == target: return True
    return dfsR(root.left, target) or dfsR(root.right, target)

def buildTree():
    a = TreeNode('a')
    b = TreeNode('b')
    c = TreeNode('c')
    d = TreeNode('d')
    e = TreeNode('e')
    f = TreeNode('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    return a

class MyTestCase(unittest.TestCase):
    def test_something(self):
        root  = buildTree()
        t1 = 'a'
        # self.assertEqual(True, dfsI(root, 'a'))  # add assertion here
        # self.assertEqual(False, dfsI(root, 'z'))
        self.assertEqual(True, dfsR(root, 'a'))  # add assertion here
        self.assertEqual(False, dfsR(root, 'z'))


if __name__ == '__main__':
    unittest.main()
