def pathsum(root, targetsum):
    output = []

    def dfs(node, path, currSum):
        currSum += node.val
        temp = path + [node.val]

        if node.left:
            dfs(node.left, temp, currSum)
        if node.right:
            dfs(node.right, temp, currSum)
        if not node.left and not node.right and currSum == targetsum:
            output.append(temp)
    if not root:
        return []
    dfs(root, [], 0)
    return output