def isSymmetryTree(root):
    if root is None:
        return True
    return isSymmetryTreeHelper(root.left, root.right)

def isSymmetryTreeHelper(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if left.val != right.val:
        return False
    return isSymmetryTreeHelper(left.left, right.right) and isSymmetryTreeHelper(left.right, right.left)