def lowestCommonAncestor2(self,root, p, q):
    self.p_val = self.q_val = False
    self.find(root,p,q)
    if not self.p_val or not self.q_val:
        return None
    return self.findLCA(root,p,q)

def find(self,root,p,q):
    if root == None:
        return None
    if root == p:
        self.p_val = True

    if root == q:
        self.q_val = True
    self.find(root.left,p,q)
    self.find(root.right,p,q)

def findLCA(self,root,p,q):
    if not root == None:
        return False
    if root == p or root == q:
            return root
    left = self.findLCA(root.left,p,q)
    right = self.findLCA(root.right,p,q)
    if left and right:
        return root
    return left if left else right
    

    
        
            
