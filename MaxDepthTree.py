"""
104 Maximum Depth
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root ==[] :
        return 0
    print maxDepth(root.left)
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
print maxDepth(root)
"""
http://fellowship.hackbrightacademy.com/materials/f17a/lectures/trees/
http://interactivepython.org/courselib/static/pythonds/Trees/Objectives.html