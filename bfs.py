import unittest

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# iterative
def bfs (root: TreeNode, target):
    if root is None: return False
    q = [root]
    while len(q) > 0:
        curr = q.pop(0)
        if target == curr.data: return True
        if curr.left: q.append(curr.left)
        if curr.right: q.append(curr.right)
    return False


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
        t1 = ['a', 'b', 'c', 'd', 'e', 'f']
        self.assertEqual(True, bfs(root, 'c'))  # add assertion here
        self.assertEqual(False, bfs(root, 'r'))


if __name__ == '__main__':
    unittest.main()