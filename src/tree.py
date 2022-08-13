class Tree:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

    #     10
    #     /\
    #    5  15
    #   /\
    #  25 35
    #      
#  Preorder -> 10,5,25,35,15
root= Tree(10)
root.left=Tree(5)
root.right=Tree(15)
root.left.left=Tree(25)
root.left.right=Tree(35)

def PreOrder(root):
    if(root==None):
        return
    print(root.data)
    PreOrder(root.left)
    PreOrder(root.right)

print(PreOrder(root))