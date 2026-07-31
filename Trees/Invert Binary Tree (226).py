class Solution(object):
    def invertTree(self, root):
        if not root: # best case
            return None

        root.left, root.right = root.right, root.left # swaps left and right pointer of the current node

        self.invertTree(root.left) # swaps all sub-trees underneath main tree too
        self.invertTree(root.right)

        return root