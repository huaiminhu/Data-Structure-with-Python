class Tree: # 樹類別
    
    def read(self): # 讀取輸入資料
        self.n = int(input())
        self.L = [[] for _ in range(self.n)]
        for _ in range(self.n - 1):
            father, child = [map(int, input().split())]
            self.L[father].append(child)
            
    def readFile(self, fileName): # 讀取檔案資料
        fp = open(fileName)
        self.n = int(fp.readline())
        self.L = [[] for _ in range(self.n)]
        for _ in range(self.n - 1):
            father, child = map(int, fp.readline().split())
            self.L[father].append(child)
            
    def findRoot(self): # 找樹根
        inDegree = [0] * self.n # 紀錄入分支度
        for i in self.L:
            for j in i:
                inDegree[j] += 1
        for i in inDegree:
            if i == 0: # 無入分支就是樹根
                return inDegree.index(i)

class BTNode: # 二元樹節點類別
    
    def __init__(self, data):
        self.left = None # 左子樹
        self.data = data
        self.right = None # 右子樹
        
class BinaryTree: # 二元樹類別
    
    def __init__(self):
        self.root = None
        
    def read(self, fileName):
        fp = open(fileName)
        self.nodes = fp.readline().split() # 節點
        self.current = 0 # 紀錄目前節點
        self.root = self.grow() # 產生二元樹
        
    def grow(self):
        d = self.nodes[self.current]
        self.current += 1
        if d == "0": return # 無左右子樹則回上一階
        subtree = BTNode(d)
        subtree.left = self.grow() # 遞迴方法產生子樹
        subtree.right = self.grow()
        return subtree
    
    def preorder(self, n): # 前序走訪(父->左子->右子)
        if not n: return # 碰到樹葉就回上一階
        print(n.data)
        self.preorder(n.left)
        self.preorder(n.right)
        
    def inorder(self, n): # 中序走訪(左子->父->右子)
        if not n: return
        self.inorder(n.left)
        print(n.data)
        self.inorder(n.right)
        
    def postorder(self, n): # 後序走訪(左子->右子->父)
        if not n: return
        self.postorder(n.left)
        self.postorder(n.right)
        self.cnodes += 1
        print(n.data)
