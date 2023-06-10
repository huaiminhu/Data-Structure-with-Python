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
            
    def order(self):
        newOrder = []
        for i in range(len(self.L)):
            for j in self.L[i]:
                if [j[1], j[0], i] not in newOrder:
                    newOrder.append([j[1], i, j[0]])
        return sorted(newOrder)
    
    def sameTest(self, edge):
        sameU = sameV = False
        for i in self.collection:
            if edge[1] == i[1] or edge[1] == i[2]:
                sameU = True
            if edge[2] == i[1] or edge[2] == i[2]:
                sameV = True
        return sameU and sameV
    
    def MCST(self):
        paths = self.order()
        self.start = paths[0][1]
        total = 0
        while self.edges < self.n - 1:
            choice = paths.pop(0)
            if not self.sameTest(choice):
                self.collection.append(choice)
                self.edges += 1
        for i in self.collection:
            total += i[0]
        return total
    
    def Dijkstra(self, vs, vd):
        dist = []
        for i in range(self.n):
            dist.append(float("inf"))
        dist[vs] = 0
        points = []
        prev = [None] * self.n
        priority = Queue()
        priority.enQueue((dist[vs], vs))
        while not priority.isEmpty():
            vx = priority.deQueue()
            points.append(vx[1])
            priority.item = []
            if vx[1] == vd:
                return vx[0], points
            for vt in self.L[vx[1]]:
                if dist[vt[0]]:
                    dist[vt[0]] = min(dist[vt[0]], vx[0] + vt[1])
                else:
                    dist[vt[0]] = vx[0] + vt[1]
                prev[vt[0]] = vx[1]
                priority.enQueue((dist[vt[0]], vt[0]))            
            priority.item.sort()

class BFS:
    
    def __init__(self, g):
        self.s = Queue()
        self.g = g
        self.visit = [False] * g.n
        
    def search(self, v):
        orders = []
        self.s.enQueue([v])
        while not self.s.isEmpty():
            for i in self.s.deQueue():
                if self.visit[i]:
                    continue
                self.s.enQueue(self.g.L[i])
                self.visit[i] = True
                orders.append(i)
            print(self.s.item)
        if False in self.visit:
            return False
        return orders

