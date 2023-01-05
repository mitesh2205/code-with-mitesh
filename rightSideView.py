def rightSideView(self, root):
    if not root:
        return []
    res = []
    queue = [root]
    while queue:
        res.append(queue[-1].val)
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res


# solve above problem with dfs

def rightsideview_dfs(self, root):
    if not root:
        return []
    res = []
    self.dfs(root, 0, res)
    return res

def dfs(self, root, level, res):
    if not root:
        return
    if level == len(res):
        res.append(root.val)
    self.dfs(root.right, level + 1, res)
    self.dfs(root.left, level + 1, res)