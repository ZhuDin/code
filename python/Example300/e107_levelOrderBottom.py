class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root):
        self.results = []
        if not root:
            return self.results
        q = [root]
        while q:
            new_q = []
            self.results.append([n.val for n in q])
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
        return list(reversed(self.results))
    
if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    results = solution.levelOrderBottom(root)
    print("input: {1,2,3}")
    print("output:", results)
