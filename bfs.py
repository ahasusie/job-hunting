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

def bfs(root):
    if root is None:
        return -1
    
    res = []
    q = deque()
    q.append(root)
    while q:
        res.append([node.val for node in q])
        s = []
        for node in q:            
            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)
        q = s

    return res

def bfsTmp(root):
    if not root:
        return -1

    res = []
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        res.append(node.val)
        if node:
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res

def symmetricTree(root):
    if not root:
        return True  
    stack = [[root.left, root.right]]
    while stack:
        left, right = stack.pop()
        if left is None and right is None:
            continue
        if left is None or right is None:
            return False
        # if left is None and right is None:
        #     continue

        if left.val == right.val:
            stack.append([left.left, right.right])
            stack.append([left.right, right.left])            
        else:
            return False
    return True


    # if root is None:
    #         return True
    # stack = [[root.left, root.right]]

    # while stack:
    #     left, right = stack.pop()        
    #     if left is None and right is None:
    #         continue
    #     if left is None or right is None:
    #         return False
    #     if left.val == right.val:                
    #         stack.append([left.left, right.right])
    #         stack.append([left.right, right.left])
    #     else:
    #         return False
    # return True




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

#print bfsTraverse(root)
#print levelOrderBottom(root)
#print bfs(root)
#print symmetricTree(root)
print bfsTmp(root)