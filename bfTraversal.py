import unittest

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# iterative
def bfTraversal (root: TreeNode):
    if root is None: return []
    q = [root]
    out = []

    while len(q) > 0:
        curr = q.pop(0)
        out.append(curr.data)
        if curr.left: q.append(curr.left)
        if curr.right: q.append(curr.right)


    return out


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
        self.assertEqual(t1, bfTraversal(root))  # add assertion here
        self.assertEqual([], bfTraversal(None))


if __name__ == '__main__':
    unittest.main()