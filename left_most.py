class TreeMode:
    def __init__(self,val=0,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        
    def find_left_most(self,root):
        queue = []
        left_most_val = None
        while queue:
            node = queue.pop(0)
            left_most_val = node.val
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return left_most_val
def main():
    root = TreeMode(1)
    root.left = TreeMode(2)
    root.right = TreeMode(3)
    root.left.left = TreeMode(4)
    root.right.left = TreeMode(5)
    root.right.left.left = TreeMode(7)
    root.right.right = TreeMode(6)
    print(root.find_left_most(root))
    
    root2 = TreeMode(2)
    root2.left = TreeMode(1)
    root2.right = TreeMode(3)
    print(root2.find_left_most(root2))

main()