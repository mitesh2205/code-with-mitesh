import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTiterator:
    def __init__(self, root: TreeNode):
        self.stack = [] # stack to store the nodes
        while root: # push all the left nodes into the stack
            self.stack.append(root) # push the root node into the stack
            root = root.left # move to the left node

    def next(self): # return the next smallest number
        top_node = self.stack.pop() # pop the top node
        cur = top_node.right # move to the right node

        while cur: # push all the left nodes into the stack
            self.stack.append(cur) # push the root node into the stack
            cur = cur.left # move to the left node
        return top_node.val # return the value of the top node

    def hasNext(self)-> bool: # return whether we have a next smallest number
        return len(self.stack) > 0 # return whether the stack is empty

    
        


        