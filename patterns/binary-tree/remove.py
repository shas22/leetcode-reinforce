# Return the minimum value node of the BST.
def minValueNode(root):
    curr = root
    # Loop through as long as 
    while curr and curr.left:
        curr = curr.left
    return curr


# Remove a node and return the root of the BST.
def remove(root, val):
    #if root is null return None
    if not root:
        return None
    
    # check if the inserting value is bigger than the root

    # if val is bigger than the val at root
    if val > root.val:
        # recurse remove function 
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        # if there is 2 or more nodes at the value 
        else:
            # find the minimum value at root.right
            minNode = minValueNode(root.right)
            # change the value ot the target node to min value 
            root.val = minNode.val
            # recurse and find the min value node duplicate at the bottom and remove
            root.right = remove(root.right, minNode.val)
    return root