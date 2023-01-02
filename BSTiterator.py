class BSTiterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        top_node = self.stack.pop()
        cur = top_node.right

        while cur:
            self.stack.append(cur)
            cur = cur.left
        return top_node.val

    def hasNext(self)-> bool:
        return len(self.stack) > 0
        


        