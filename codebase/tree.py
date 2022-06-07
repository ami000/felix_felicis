class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    def printTree(self):
        spaces = ' ' * self.getLevel() * 3
        prefix = spaces + '|-- ' if self.parent else '>>'
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.printTree()

    def printTreeToLevel(self, nlevel):
        selfLevel = self.getLevel()
        spaces = ' ' * selfLevel * 3
        prefix = spaces + '|-- ' if self.parent else '||'
        if selfLevel <= nlevel:
            print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.printTreeToLevel(nlevel)

        pass

    def printTreeWithVariation(self, printType):
        spaces = ' ' * self.getLevel() * 3
        prefix = spaces + '|-- ' if self.parent else '||'
        if printType == 'name':
            print(prefix + self.data[0])
        elif printType == 'designation':
            print(prefix + self.data[1])
        else:
            print(prefix + self.data[0] + ' (' + self.data[1] + ')')
        if self.children:
            for child in self.children:
                child.printTreeWithVariation(printType)
    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
def build_product_tree():
    root = TreeNode('Electronics')
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.printTree()

