from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def bfsTraverse(root):   
    ret = []
    if not root:
        return ret

    stack = [root]
    while stack:
        ret.append([node.val for node in stack])
        new_q = []
        for node in stack:
            if node.left:
                new_q.append(node.left)
            if node.right:
                new_q.append(node.right)
        stack = new_q

    return ret

def levelOrderBottom(root):
    queue, res = deque([(root, 0)]), []
    while queue:
        node, level = queue.popleft()
        if node:
            if len(res) < level+1:
                res.insert(0, [])
            res[-(level+1)].append(node.val)
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
    return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

#print bfsTraverse(root)
print levelOrderBottom(root)