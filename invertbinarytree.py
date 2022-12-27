def invert_binary_tree(self,root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    self.invert_binary_tree(root.left)
    self.invert_binary_tree(root.right)
    return root
