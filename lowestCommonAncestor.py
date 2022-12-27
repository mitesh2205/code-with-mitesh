def lowest_common_Ancestor(self, root,p,q):
    if root == None or p ==root or q ==root: # if root is None or p or q is root, return root
        return root

    left, right = self.lowest_common_Ancestor(root.left,p,q), self.lowest_common_Ancestor(root.right,p,q) # left and right are the lowest common ancestor of p and q in left and right subtree respectively

    if left == None: # if left is None, return right
        return right
    elif right == None: # if right is None,
        return left
    else:
        return root # if left and right are not None, return root
