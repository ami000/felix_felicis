import unittest

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# iterative
def dfTraversalI (root: TreeNode):
    if root is None: return []
    stack = [root]
    out = []
    while len(stack) > 0:
        curr = stack.pop()
        out.append(curr.data)
        if curr.right: stack.append(curr.right)
        if curr.left: stack.append(curr.left)
    return out

# recursive

def dfTraversalR (root:TreeNode):
    if root is None: return []
    leftValues = dfTraversalR(root.left)
    rightValues = dfTraversalR(root.right)
    return [root.data, *leftValues, *rightValues]

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
        t1 = ['a', 'b', 'd', 'e', 'c', 'f']
        # self.assertEqual(t1, dfTraversalI(root))  # add assertion here
        # self.assertEqual([], dfTraversalI(None))
        self.assertEqual(t1, dfTraversalR(root))
        self.assertEqual([], dfTraversalR(None))


if __name__ == '__main__':
    unittest.main()
