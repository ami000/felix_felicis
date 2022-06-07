from tree import TreeNode

def buildCountriesTree():
    root = TreeNode('Global')
    Country_India = TreeNode('India')
    State_Gujarat = TreeNode('Gujarat')
    State_Gujarat.add_child(TreeNode('Ahmedabad'))
    State_Gujarat.add_child(TreeNode('Baroda'))

    State_Karnataka = TreeNode('Karnataka')
    State_Karnataka.add_child(TreeNode('Bengaluru'))
    State_Karnataka.add_child(TreeNode('Mysore'))

    Country_India.add_child(State_Gujarat)
    Country_India.add_child(State_Karnataka)

    Country_USA = TreeNode('USA')
    State_New_Jersey = TreeNode('New Jersey')
    State_New_Jersey.add_child(TreeNode('Princeton'))
    State_New_Jersey.add_child(TreeNode('Trenton'))

    State_California = TreeNode('California')
    State_California.add_child(TreeNode('San Francisco'))
    State_California.add_child(TreeNode('Mountain View'))
    State_California.add_child(TreeNode('Palo Alto'))

    Country_USA.add_child(State_New_Jersey)
    Country_USA.add_child(State_California)

    root.add_child(Country_India)
    root.add_child(Country_USA)
    return root

if __name__ == '__main__':
    root = buildCountriesTree()
    root.printTreeToLevel(0)