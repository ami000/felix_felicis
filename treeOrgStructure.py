from tree import  TreeNode

def buildManagementTree():
    root = TreeNode(('Nilupul', 'CEO'))
    cto = TreeNode(('Chinmay', 'CTO'))
    hr = TreeNode(('Gels', 'HR Head'))

    infra = TreeNode(('Vishwa', 'Infrastructure Head'))
    app = TreeNode(('Aamir', 'Application Head'))

    infra.add_child(TreeNode(('Dhaval', 'Cloud Manager')))
    infra.add_child(TreeNode(('Abhijit', 'App Manager')))

    cto.add_child(infra)
    cto.add_child(app)

    hr.add_child(TreeNode(('Peter', 'Recruitment Manager')))
    hr.add_child(TreeNode(('Waqas', 'Policy Manager')))


    root.add_child(cto)
    root.add_child(hr)
    return root

if __name__ == '__main__':
    root = buildManagementTree()
    root.printTreeWithVariation("name")  # prints only name hierarchy
    root.printTreeWithVariation("designation")  # prints only designation hierarchy
    root.printTreeWithVariation("both")  # prints both (name and designation) hierarchy