class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    def diameter_of_binary_tree(self, root):
        diameter = [0]
        def helper(node):
            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            diameter[0] = max(diameter[0], left + right)
            
            return max(left, right) + 1
        
        helper(root)
        return diameter[0]
def main():

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(root.diameter_of_binary_tree(root))
    
    root2 = Node(1)
    root2.left = Node(2)
    print(root2.diameter_of_binary_tree(root2))
    
if __name__ == '__main__':
    main()