from stackClass import Stack
from QueueClass import Queue

class GraphMatrix: # 圖的鄰接矩陣類別
    
    def read(self): # 讀取輸入資料
        self.n = int(input()) # n : 頂點數
        self.L = [[] for _ in range(self.n)]
        for i in range(self.n): # 串列L紀錄各頂點之鄰點
            self.L[i] = [map(int, input().split())]
        
    def readFile(self, fileName): # 從檔案讀取資料
        fp = open(fileName, "r")
        self.n = int(fp.readline())
        self.L = [[] for _ in range(self.n)]
        for i in range(self.n):
            self.L[i] = [map(int, fp.readline().split())]
            
class GraphList: # 圖的鄰接串列類別
    
    def read(self):
        # e : 邊的數量
        self.n, self.e = map(int, input().split())
        self.L = [[] for _ in range(self.n)]
        for _ in range(self.e):
            i, j = map(int, input().split())
            self.L[i].append(j)
        
    def readFile(self, fileName):
        fp = open(fileName, "r")
        self.n, self.e = map(int, fp.readline().split())
        self.L = [[] for _ in range(self.n)]
        for _ in range(self.e):
            i, j = map(int, fp.readline().split())
            self.L[i].append(j)
            
    def AOV(self): # 頂點工作網路
        inDegree = [0] * self.n # inDegree串列存放各頂點入分支度
        for i in self.L:
            for j in i:
                inDegree[j] += 1 # 計算各頂點入分支度
        doing = Queue() # doing佇列存放正在進行的工作(頂點)
        orders = [] # orders串列存放依序完成的工作
        finish = [False] * self.n # finish紀錄工作完成與否
        for i in inDegree:
            if i == 0: # 把源點加入doing
                doing.enQueue(inDegree.index(i))
        while not all(finish): # 執行至所有工作皆完成
            if doing.isEmpty(): # doing為空表示有環路
                return False
            pre = doing.deQueue() # 工作完成後離開doing
            finish[pre] = True # 完成工作就是True
            orders.append(pre) # 紀錄完成的工作
            for suc in self.L[pre]: # 走訪頂點入分支
                inDegree[suc] -= 1 # 對應pre的頂點入分支扣掉一
                if inDegree[suc] == 0:
                    doing.enQueue(suc) # 入分支為0表可進行該頂點工作
        return orders

class WtGraph: # 加權圖鄰接串列類別

    def read(self):
        self.n, self.e = map(int, input().split())
        self.L = [[] for _ in range(self.n)]
        for _ in range(self.e):
            u, v, w = map(int, input().split())
            self.L[u].append((v, w)) # v為鄰點, w為加權數
        
    def readFile(self, fileName):
        fp = open(fileName, "r")
        self.n, self.e = map(int, fp.readline().split())
        self.L = [[] for _ in range(self.n)]
        for _ in range(self.e):
            u, v, w = map(int, fp.readline().split())
            self.L[u].append((v, w))