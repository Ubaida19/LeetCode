# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/?envType=daily-question&envId=2024-01-24
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def psuedo_palindromic(self, root)->int:
        digits = [0]*10
        return self.dfs(root, digits)

    
    def dfs(self, root, digits)->int:
        if root is None:
            return 0
        
        digits[root.val] += 1
        if root.left is None and root.right is None:
            count_odd = self.count_odd(digits)
            digits[root.val] -= 1
            if count_odd < 2:
                return 1
            else:
                return 0
                        
        left_count = self.dfs(root.left, digits)
        right_count = self.dfs(root.right, digits)
        
        digits[root.val] -= 1
        return left_count + right_count
        
        
    def count_odd(self, digits):
        odd_count = 0
        i:int = 1
        while i < 10 and odd_count < 2:
            if digits[i] % 2 == 1:
                odd_count += 1
            i += 1
        return odd_count
            
def main():
    root1 = TreeNode(2)
    root1.left = TreeNode(3)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(1)
    root1.right.right = TreeNode(1)
    print(root1.psuedo_palindromic(root1))
    
    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(1)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(3)
    root2.left.right.right = TreeNode(1)
    
    print(root2.psuedo_palindromic(root2))
    
if __name__ == '__main__':
    main()