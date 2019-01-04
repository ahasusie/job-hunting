# need to practice:
# 1. BFS
# 2. DFS iteration/recursion
# 3. DFS traversal/divide & conquer 
#     -divide and conquer: post order, handle buttom-up
#       1) go to leaf:
#             def foo(root):
#                 left = foo(root.left)
#                 right = foo(root.right)
#       2) do sth to the leaves, and return to upper level

#     -traversal ususally: pre order, handle top-down
#       1) set some global variables
#       2) use dfs() to do the preorder traversal part of work
#       3) return
# 4. graphs
# 5. stack and queue usage in tree/graphs
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# BFS traversal
def printTree(root):
    if not root:
        return 
    res = []
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        if node:
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return res

# 226. invert binary tree 
# DFS, iteration
# DFS, recursion, divide and conquer
def invertBinaryTree(root):
    # buttom-up, DFS recursion divide and conquer, post order
    # ??? how to return in recursion ???
    if not root:
        return
    left = invertBinaryTree(root.left)
    right = invertBinaryTree(root.right)
    root.left = right
    root.right = left
    return root

    # iteration, preorder, stack
    # ??? stack append order: left and right who append first ???
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)            
    return root

    # BFS
    if not root:
        return
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        if node:
            node.left, node.right = node.right, node.left
            q.append(node.left)
            q.append(node.right)
    return root

def preorder(root):
    if not root:
        return
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)                                   
    return res

# 104
# bfs iteration
# dfs iteration 
# dfs recursion traversal 
# dfs recursion divide and conquer
def maxDepth(root):
    # bfs iteration, top-down
    if not root:
        return 
    depth = 0
    q = deque()
    q.append([root, 1])
    while q:
        node, curDepth = q.popleft()
        if node:
            depth = max(depth, curDepth)
            if node.left:
                q.append([node.left, curDepth+1]) 
            if node.right:
                q.append([node.right, curDepth+1])            
    return depth

    # dfs iteration, top-down, preorder
    if not root:
        return
    depth = 0
    stack = [(root, 1)]
    while stack:
        node, curDepth = stack.pop()
        if node:
            depth = max(depth, curDepth)
            if node.right:
                stack.append((node.right, curDepth+1))
            if node.left:
                stack.append((node.left, curDepth+1))
    return depth

    # dfs recursion, divide and conquer, post order, buttom-up
    max depth = left/right subtree max depth + 1
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

# dfs recursion, traversal, top-down
class Solutions(object):
    def maxDepth(self, root):
        self.max_depth = 0
        self.dfs(root, 1)
        return self.max_depth
    
    def dfs(self, root, depth):
        if not root:
            return 0
        self.max_depth = max(depth, self.max_depth)
        self.dfs(root.left, depth+1)
        self.dfs(root.right, depth+1)

# 110. balanced binary tree
# dfs, recursion, divide and conquer
# dfs, iteration
def isBalancedTree(root):
    # # use dfs recursion, divide and conquer to get depth
    # def dfs(root):
    #     if not root:
    #         return 0
    #     # recursively check depth of left, right
    #     left = dfs(root.left)
    #     right = dfs(root.right)
    #     # do some check on depth each time, is balanced?
    #     if abs(left-right) > 1 or left == -1 or right == -1:
    #         return -1
    #     return max(left, right)+1
    # return dfs(root) != -1

    # dfs, iteration
    stack, node, last, depths = [], root, None, {}
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack[-1]
            if not node.right or last == node.right:
                node = stack.pop()
                left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
                if abs(left - right) > 1: return False
                depths[node] = 1 + max(left, right)
                last = node
                node = None
            else:
                node = node.right
    return True    

# 257. binary tree path
# dfs, iteration, traversal, with level, preorder
# dfs, recursion, traversal
# dfs, recursion, divide and conquer
# when needs to reserve value from upper level, can use (root, "1") etc.
def binaryTreePaths(root):
    # dfs, iteration, traversal, with level, preorder
    # res = []
    # if not root:
    #     return res
    # stack = [[root, ""]]
    # while stack:
    #     node, path = stack.pop()
    #     if not node.left and not node.right:
    #         res.append(path+str(node.val))
    #     if node and node.right:
    #         stack.append([node.right, path+str(node.val)+"->"])
    #     if node and node.left:
    #         stack.append([node.left, path+str(node.val)+"->"])
    # return res

    # # dfs, recursion, traversal, preorder
    # res = []
    # if not root: return res
    # path = ""
    # def dfs(root, path, res):
    #     if not root.left and not root.right:
    #         res.append(path+str(root.val))
    #     if root.left:
    #         dfs(root.left, path+str(root.val)+"->", res)
    #     if root.right:
    #         dfs(root.right, path+str(root.val)+"->", res)
    # dfs(root, path, res)
    # return res

    # dfs, recursion, divide and conquer
    res = []
    if not root: return res
    leftPath = binaryTreePaths(root.left)
    rightPath = binaryTreePaths(root.right)

    if not root.left and not root.right:
        res.append(str(root.val))

    if root.left:       
        #print "left: ", leftPath 
        for path in leftPath:
            path = str(root.val)+"->"+path
            res.append(path)
    if root.right:
        #print "right: ", rightPath
        for path in rightPath:
            path = str(root.val)+"->"+path
            res.append(path)
    return res

# 114. flatten binary tree
# reversed preorder, dfs, recursion, divide and conquer, buttom-up
# dfs, iteration, preorder
def flatten(root):
    # dfs iteration
    if not root:
        return None
    newRoot = TreeNode(-1)
    stack = [root]
    while stack:
        node = stack.pop()
        newRoot.right = node
        newRoot.left = None
        if node:
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        newRoot = node
    return root

    # recursion, reversed preorder, divide and conquer, buttom-up
    # ??? python variable scope, namespace, nested functions ???
    # tmp = TreeNode(-1)
    # def dfs(root):
    #     nonlocal tmp
    #     if not root: return None
    #     dfs(root.left)
    #     dfs(root.right)

    #     root.right = tmp
    #     root.left = None
    #     tmp = root
    # dfs(root)

# reversed preorder, dfs, recursion, divide and conquer, buttom-up
class flattenSolutions(object):
    def __init__(self):
        self.prev = None
    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root

# find the closest value to X in binary search tree
def closestBSTValue(root, x):
    # recursion
    if not root:
        return "not found"

    if x < root.val:
        left = closestBSTValue(root.left, x)
    if x > root.val:
        right = closestBSTValue(root.right, x)
    
    return root.val

root = TreeNode(6)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

print closestBSTValue(root, 5)

# flatten(root)
# print printTree(root)
# obj = flattenSolutions()
# obj.flatten(root)
# print printTree(root)
#print printTree(flatten(root))
#print binaryTreePaths(root)
#print isBalancedTree(root)
#obj = Solutions()
#print obj.maxDepth(root)
#print maxDepth(root)
#invertBinaryTree(root)
#print printTree(root)




