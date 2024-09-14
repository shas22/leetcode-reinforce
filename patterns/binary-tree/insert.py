class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None


def insertNode(root, val):
    if not root:
        return TreeNode(val)
    
def minValueNode(root):
    curr = root

    # while current is not null and current.left is not null
    while curr and curr.left:
        curr = curr.left
    return curr


def removeNode(root, val):
    if not root:
        return None
    
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    return root





'''
Initial tree:
      4
    /   \
   2     6
  / \   / 
 1   3 5   

Stack visualization:
(bottom of stack at the top, top of stack at the bottom)

1. Initial call:
|-------------------------|
| remove(root=4, val=4)   |
|-------------------------|

2. After realizing both children exist and finding minValueNode:
|-------------------------|
| remove(root=4, val=4)   |
| minValue = 5            |
|-------------------------|

3. Recursive call to remove 5 from right subtree:
|-------------------------|
| remove(root=4, val=4)   |
| minValue = 5            |
|-------------------------|
| remove(root=6, val=5)   |
|-------------------------|

4. Another recursive call to remove 5:
|-------------------------|
| remove(root=4, val=4)   |
| minValue = 5            |
|-------------------------|
| remove(root=6, val=5)   |
|-------------------------|
| remove(root=5, val=5)   |
|-------------------------|

5. After removing 5 (it returns null as it has no children):
|-------------------------|
| remove(root=4, val=4)   |
| minValue = 5            |
|-------------------------|
| remove(root=6, val=5)   |
| root.left = null        |
|-------------------------|

6. After returning from remove(root=6, val=5):
|-------------------------|
| remove(root=4, val=4)   |
| minValue = 5            |
| root.val = 5            |
| root.right updated      |
|-------------------------|

7. Final return to the main program:
(empty stack)

Resulting tree:
      5
    /   \
   2     6
  / \     
 1   3    

'''
