class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
def printTree(root):
    if not root:
        return None
    ret = []
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        if node:
            ret.append(node.val)
            q.append(node.left)
            q.append(node.right)        
    print ret

def preorder(root):
    if not root:
        return None
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            # if node.left:
            #     stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return res
    ###########################################
    res = []
    def dfs(node):
        if not node:
            return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return res

def inorder(root):
    ret = []
    def dfs(node):
        if not node:
            return 
        dfs(node.left)
        ret.append(node.val)
        dfs(node.right)
    dfs(root)
    return ret

def postorder(root):
    ret = []
    def dfs(node):
        if not node:
            return 
        dfs(node.left)
        dfs(node.right)
        ret.append(node.val)
    dfs(root)
    return ret

# dfs, recursion, divide and conquer, postorder, buttom-up
def maxDepth(root):
    if not root:
        return 0
    l = maxDepth(root.left) 
    r = maxDepth(root.right)
    ans = max(l, r)+1
    return ans

# dfs, recursion, traversal, preorder top down
class Solution(object):
    def maxDepth(self, root):
        self.ans = 0
        self.dfs(root, 1)
        return self.ans
    def dfs(self, node, depth):
        if not node:
            return
        self.ans = max(self.ans, depth)
        self.dfs(node.left, depth+1)
        self.dfs(node.right, depth+1)

#226. 
# dfs, recursion, divide and conquer, top-down
# dfs, recursion, divide and conquer, buttom-up 
# bfs, iteration, top-down 
def invertTree(root):
    # if not root:
    #     return 
    # root.left, root.right = root.right, root.left
    # invertTree(root.left)
    # invertTree(root.right)
    # return root

    # if not root:
    #     return
    # left = invertTree(root.left)
    # right = invertTree(root.right)
    # root.left, root.right = right, left
    # return root

    if not root: return 
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            node.left, node.right = node.right, node.left
            q.append(node.left)
            q.append(node.right)
    return root

#110.
#dfs, recursion, devide and conquer, postorder buttom up 
def balanceTree(root):
    def dfs(node):
        if not node:
            return 0
        left = balanceTree(node.left)
        right = balanceTree(node.right)
        if abs(left-right) > 1:
            return -1
        return max(left, right)+1
    return dfs(root) != -1

#257
#dfs, recursion, traversal, preorder top down
class treePathSolution(object):
    def treePath(self, root):
        if not root: return None
        self.res = []
        self.dfs(root, "")
        return self.res
    def dfs(self, node, path):
        path = path+str(node.val)
        if not node.left and not node.right:
            self.res.append(path)
        if node.left:
            self.dfs(node.left, path+"->")
        if node.right:
            self.dfs(node.right, path+"->")

#114
#dfs, recursion, traversal, reversed preorder buttom up, need global variable
class flattenTreeSolution(object):
    def __init__(self):
        self.prev = None
    def flattenTree(self, root):
        if not root: return None
        self.flattenTree(root.right)
        self.flattenTree(root.left)        
        root.right = self.prev
        root.left = None
        self.prev = root
#dfs, iteration, traversal, preorder top down
def flattenTree(root):
    if not root: return None
    tmp = Node(None)
    stack = [root]
    while stack:
        node = stack.pop()
        tmp.right = node
        tmp.left = None
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)      
        tmp = node

####################################################################
# BST
# 270
class closestValueBSTSolution(object):
    #dfs, recursion, divide and conquer, postorder buttom up
    def closestValueBST1(self, root, target):
        if not root: return None
        if target < root.val:
            if root.left:
                left = self.closestValueBST1(root.left, target)
                if abs(left - target) < abs(root.val - target):
                    return left
        if target > root.val:
            if root.right:
                right = self.closestValueBST1(root.right, target)
                if abs(right - target) < abs(root.val - target):
                    return right
        return root.val

    #dfs, recursion, traversal, preorder top down
    def closestValueBST2(self, root, target):
        self.res = root.val
        self.dfs(root, target)
        return self.res
    def dfs(self, root, target):
        if not root: return None
        if abs(self.res - target) > abs(root.val - target):
            self.res = root.val
        if target < root.val:
            left = self.dfs(root.left, target)
        else:
            right = self.dfs(root.right, target)

#find floor of a given number in BST
def floorBST(root, target):
    if not root: return None
    if root.val == target:
        return root
    if root.val > target:
        return floorBST(root.left, target)
    node = floorBST(root.right, target)
    if node:
        return node
    else:
        return root
class floorBSTSolution(object):
    def floorBST(self, root, target):
        self.res = None
        self.dfs(root, target)
        return self.res
    def dfs(self, root, target):
        if not root: return None
        if target > root.val:
            self.res = root.val
            self.dfs(root.right, target)
        else:
            self.dfs(root.left, target)

#find ceil of a given number in BST
def ceilBST(root, target):
    if not root: return -1
    if root.val == target:
        return root.val
    if root.val < target:
        return ceilBST(root.right, target)
    value = ceilBST(root.left, target)
    if value >= target:
        return value
    else:
        return root.val
#只要比p.val大，该root就可能成为p的继承者，不断的递归缩小root的值，最后就会返回比p.val大的最小值。如果没有比p.val大的值，直接返回None即可
class ceilBSTSolution(object):
    def ceilBST(self, root, p):
        self.res = None
        self.dfs(root, p)
        return self.res        
    def dfs(self, root, p):
        if not root: return
        if p < root.val:
            self.res = root.val
            self.dfs(root.left, p)
        else:
            self.dfs(root.right, p)

#search range in BST
def rangeBST(root, lo, hi):
    if not root: return None
    if lo < root.val:
        rangeBST(root.left, lo, hi)
    if lo <= root.val <= hi:
        print root.val
    if root.val < hi:
        rangeBST(root.right, lo, hi)

#230. Kth smallest item in BST
class KthSmallestSolution(object):
    def kthSmallestBST(self, root, k):
        self.res = None
        self.count = k
        self.inorder(root)
        return self.res
    def inorder(self, root):
        if not root: return 
        self.inorder(root.left)
        self.count -= 1
        if self.count == 0:
            self.res = root.val
            return 
        self.inorder(root.right)
#235. Lowest Common Ancestor in BST
#dfs, recursion, divide and conquer
def lcaBST(root, n1, n2):
    if not root: return
    if root.val > max(n1, n2):
        return lcaBST(root.left, n1, n2)
    if root.val < min(n1, n2):
        return lcaBST(root.right, n1, n2)
    if n1 <= root.val <= n2:
        return root

#98. validate a BST
#dfs, traversal
class validBSTSolution(object):    
    def validBST(self, root):
        self.arr = []
        self.inorder(root)
        return self.arr == sorted(self.arr) and len(self.arr) == len(set(self.arr))
        
    def inorder(self, root):
        if not root: return 
        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)

# end of BST practice
########################################################

#111. min depth of a tree
def minDepth(root):
    #dfs, recursion, divide and conquer, postorder buttom-up
    if not root: return 0
    l = minDepth(root.left)
    r = minDepth(root.right)
    if l == 0 or r == 0:
        return 1
    return min(l, r)+1

    #bfs, iteration, traversal
    if not root: return 0
    q = deque([(root, 1)])
    while q:
        node, depth = q.popleft()
        children = [node.left, node.right]
        if not any(children):
            return depth
        for c in children:
            if c:
                q.append((c, depth+1)) 

#112. path sum
#dfs, recursion, divide and conquer, preorder top-down
def pathSum(root, sum):
    if not root: return False
    if not root.left and not root.right:    #leaves
        return sum == root.val
    sum = sum-root.val
    left = pathSum(root.left, sum)
    right = pathSum(root.right, sum)
    return left or right
#dfs, recursion, traversal, preorder top-down
class pathSumSolution(object):
    def pathSum(self, root, sum):
        self.res = set()
        self.dfs(root, 0)
        return True if sum in self.res else False
    def dfs(self, root, tmp):
        if not root: return
        tmp += root.val
        if not root.left and not root.right:    #leaves
            self.res.add(tmp)        
        self.dfs(root.left, tmp)
        self.dfs(root.right, tmp)

#113. all path sum
#dfs, recursion, traversal, preorder top-down
class allPathSumSolution(object):
    def allPathSum(self, root, t):
        self.ans = []
        self.dfs(root, t, [])
        return self.ans
    def dfs(self, root, t, tmp):
        if not root: return 
        if not root.left and not root.right:
            tmp.append(root.val)
            if sum(tmp) == t: 
                self.ans.append(tmp)      
        self.dfs(root.left, t, tmp+[root.val])
        self.dfs(root.right, t, tmp+[root.val])

#437. path sum III
#dfs, recursion, traversal, preorder top-down
class pathSumIIISolution(object):
    def __init__(self):
        self.res = 0
    def pathSumIII(self, root, target): #everynode in tree should have a check like it's the root
        if not root: return 0
        self.dfs(root, target)
        self.pathSumIII(root.left, target)
        self.pathSumIII(root.right, target)
        return self.res
    def dfs(self, root, target):    #check on every tree node
        if not root: return
        if target == root.val:
            self.res += 1
        self.dfs(root.left, target-root.val)
        self.dfs(root.right, target-root.val)

#108. convert sorted array to BST
#dfs, recursion, divide and conquer
def convertToBst(arr):
    def dfs(arr, l, r):
        if l>r: return 
        mid = l+(r-l)//2
        node = Node(arr[mid])
        node.left = dfs(arr, l, mid-1)
        node.right = dfs(arr, mid+1, r)
        return node   
    return dfs(arr, 0, len(arr)-1)

#100. same tree
def sameTree(r1, r2):
    #dfs, recursion, divide and conquer, preorder top-down
    if not r1 or not r2: return r1 == r2
    if r1.val != r2.val:
        return False
    left = sameTree(r1.left, r2.left)
    right = sameTree(r1.right, r2.right)
    return left and right

    #dfs, iteration, traversal
    stack = [(r1, r2)]
    while stack:
        node1, node2 = stack.pop()
        if not node1 and not node2: continue
        if not node1 or not node2: return node1 == node2
        if node1.val != node2.val:
            return False
        stack.append((r1.right, r2.right))
        stack.append((r1.left, r2.left))
    return True  

#101. symmetric tree
def symmetricTree(root):
    #dfs, recursion, divide and conquer, preorder top-down
    if not root: return True
    def dfs(n1, n2):
        if not n1 or not n2: return n1 == n2
        if n1.val != n2.val: return False
        return dfs(n1.left, n2.right) and dfs(n1.right, n2.left)
    return dfs(root.left, root.right)

    # #bfs, iteration, traversal
    q = deque([root.left, root.right])
    while q:
        n1 = q.popleft()
        n2 = q.popleft()
        if not n1 and not n2: continue
        if not n1 or not n2: return False
        if n1.val != n2.val: return False
        q.append(n1.left)
        q.append(n2.right)
        q.append(n1.right)
        q.append(n2.left)
    return True

#543. Diameter of tree
#dfs, recursion, left max length + right max length, postorder buttom up
class diaTreeSolution(object):
    def diameterOfBinaryTree(self, root):
        self.res = 0
        self.dfs(root)
        return self.res    
    def dfs(self, root):
        if not root: return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.res = max(self.res, left + right)
        return max(left, right) + 1

#splitBST
#dfs, recursion, divide and conquer
def splitBST(root, target):
    if not root: return [None, None]
    if root.val > target:
        left, right = splitBST(root.left, target)
        root.left = right
        return [left, root]
    else:
        left, right = splitBST(root.right, target)
        root.right = left
        return [root, right]

# build tree from preorder/inorder
# recursion
def buildTree(preorder, inorder):
    if inorder:
        index = inorder.index(preorder.pop(0))
        root = Node(inorder[index])
        root.left = buildTree(preorder, inorder[:index])
        root.right = buildTree(preorder, inorder[index+1:])
        return root

# 652 find duplicate trees
def findDuplicateSubtrees(root):
    pass

# 814. tree pruning: remove all the subtrees that contains 0
# dfs, recursion, divide and conquer, postorder buttom up 
def treePruning(root):
    if not root: return
    root.left = treePruning(root.left)
    root.right = treePruning(root.right)
    if not root.left and not root.right and not root.val:
        return None
    return root

#662. max width of a tree, (node index, level related problem)
#dfs, recursion, traversal, preorder top-down
class treeMaxWidthSolution(object):
    def widthOfBinaryTree(self, root):
        self.ans = 0
        left = {}
        def dfs(node, depth = 0, pos = 0):
            if node:
                left.setdefault(depth, pos)
                self.ans = max(self.ans, pos - left[depth] + 1)
                dfs(node.left, depth + 1, pos * 2)
                dfs(node.right, depth + 1, pos * 2 + 1)
        dfs(root)
        return self.ans
#bfs, preorder top-down
def widthOfBinaryTree(root):
    ans = 0
    queue = [(root, 0, 0)]
    cur_depth = left = ans = 0
    for node, depth, pos in queue:
        if node:
            queue.append((node.left, depth+1, pos*2))
            queue.append((node.right, depth+1, pos*2 + 1))
            if cur_depth != depth:
                cur_depth = depth
                left = pos
            ans = max(pos - left + 1, ans)
    return ans


#366. find leaves of every same level of a tree
#dfs, recursion, divide and conquer, postorder buttom-up
class findLeavesSolution(object):
    def findLeaves(self, root):
        self.ans = []
        self.dfs(root)
        return self.ans    
    def dfs(self, root):
        if not root: return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        height = max(left, right)+1
        if len(self.ans) < height:
            self.ans.append([])
        self.ans[height-1].append(root.val)
        return height


if __name__ == "__main__":
    root = Node(1) 
    root.left      = Node(2) 
    root.right     = Node(0) 
    root.left.left  = Node(1) 
    root.left.right  = Node(3) 
    root.right.left = Node(0)
    root.right.right = Node(1)

    print widthOfBinaryTree(root)
    # obj = findLeavesSolution()
    # print obj.findLeaves(root)
    # obj = treeMaxWidthSolution()
    # print obj.widthOfBinaryTree(root)
    # printTree(treePruning(root))
    # preorder = [3,9,20,15,7]
    # inorder = [9,3,15,20,7]
    # printTree(buildTree(preorder, inorder))
    # ret = splitBST(root, 2)
    # printTree(ret[0])
    # printTree(ret[1])
    # obj = diaTreeSolution()
    # print obj.diameterOfBinaryTree(root)
    # print symmetricTree(root)
    # arr = [0,3,6,9,10,11,15]
    # node = convertToBst(arr)
    # printTree(Node)
    # root1 = Node(9) 
    # root1.left      = Node(3) 
    # root1.right     = Node(2) 
    # root1.left.left  = Node(0) 
    # root1.left.right  = Node(6) 
    # root1.right.left = Node(7)
    # root1.right.right = Node(15)

    # root2 = Node(9) 
    # root2.left      = Node(3) 
    # root2.right     = Node(2) 
    # root2.left.left  = Node(0) 
    # root2.left.right  = Node(6) 
    # root2.right.left = Node(7)
    # root2.right.right = Node(15)

    # print sameTree(root1, root2)
    # obj = pathSumIIISolution()
    # print obj.pathSumIII(root, 18)
    # print pathSum(root, 18)
    # obj = floorBSTSolution()
    # print obj.floorBST(root, 5)
    # obj = ceilBSTSolution()
    # print obj.ceilBST(root, 5)
    # print minDepth(root)
    # obj = validBSTSolution()
    # print obj.validBST(root)
    # n = lowestCommonAncestor(root, 3, 10)
    # print n.val
    # obj = KthSmallestSolution()
    # print obj.kthSmallestBST(root, 3)
    # rangeBST(root, 2, 12)
    # n=floorBST(root, 12)
    # print n.val
    # print ceilBST(root, 5)
    # obj = closestValueBSTSolution()
    # print obj.closestValueBST1(root, 5)
    # print closestValueBST(root, 2)
    # print floorBST(root, 2)
    # obj = flattenTreeSolution()
    # obj.flattenTree(root)
    # flattenTree(root)
    # printTree(root)
    # obj = treePathSolution()
    # print obj.treePath(root)
    #print balanceTree(root)
    # printTree(invertTree(root))
    # print preorder(root)
    # print inorder(root)
    # print postorder(root)
    # print maxDepth(root)
    # obj = Solution()
    # print obj.maxDepth(root)