class ListNode: # 節點類別
    
    def __init__(self, data = 0):
        self.data = data # 節點資料
        self.nxt = None # 下個節點
        
class LinkedList: # 鏈結串列類別
    
    def __init__(self):
        self.head = None # 指標
        self.size = 0
        
    def length(self):
        return self.size
    
    def append(self, value): # 新增節點
        p = self.head # 設定指標
        if p == None: # 無節點則指向新的節點
            self.head = ListNode(value)
        else:
            while p.nxt:
                p = p.nxt
            p.nxt = ListNode(value) # 在鏈結串列尾端新增節點
        self.size += 1
                
    def insert(self, p, value): # 插入節點
        node = ListNode(value)
        node.nxt = p.nxt # 新節點的下個節點設為原節點的下個節點
        p.nxt = node # 原節點的下個節點設為新節點
        self.size += 1
        
        
    def find(self, value): # 尋找節點
        p = self.head
        while p:
            if p.data == value:
                return p
            p = p.nxt
        return None
    
    def delete(self, value): # 刪除節點
        pre = None # pre指向第一個節點之前
        old = self.head # old指向第一個節點
        while old:
            if old.data == value: # 找到要刪除的節點
                break
            pre = old
            old = old.nxt
        if old:
            if pre == None: # 刪除第一個節點
                pre = old.nxt
                del old
                return pre
            pre.nxt = old.nxt # pre的下個節點越過old設為old的下個節點
            del old # 刪除節點
        self.size -= 1
        return self.head
    
    def traversal(self): # 走訪鏈結串列
        p = self.head
        while p:
            print(p.data)
            p = p.nxt
            
    def reverse(self): # 反轉鏈結串列
        if self.size < 2: # 只有一個節點無法反轉
            return
        p = self.head # 設定p,q,r三個指標
        q = p.nxt
        r = q.nxt
        p.nxt = None # p的下個節點設為原鏈結串列之前
        while q: # 走訪鏈結串列至q指向最後一個節點
            q.nxt = p # 使用指標q反轉(指向前一節點)
            p = q
            q = r
            if r: # 避免漏掉最後一個節點
                r = r.nxt
        self.head = p
        
    def rev2(self, p, q, r): # 使用遞迴方式反轉
        if self.size < 2:
            return
        if r == None: # 第三個指標r若沒資料則停止走訪
            q.nxt = p # 反轉最後一個節點指向
            self.head = q # 第二個指標q設為第一節點
        else:
            self.rev2(q, r, r.nxt)
            q.nxt = p # 反轉

class CLinkedList: # 環狀鏈結串列
    
    def __init__(self):
        self.head = None
        self.size = 0
        
    def length(self):
        return self.size
    
    def append(self, value):
        p = self.head
        node = ListNode(value)
        if p == None:
            self.head = node
        else:
            while p.nxt:
                p = p.nxt
            p.nxt = node
        self.size += 1
        node.nxt = self.head # 新節點的下個節點設為第一個節點
                
    def insert(self, p, value):
        node = ListNode(value)
        node.nxt = p.nxt
        p.nxt = node
        self.size += 1
        
        
    def find(self, value):
        p = self.head
        while p:
            if p.data == value:
                return p
            p = p.nxt
        return None
    
    def delete(self, value):
        pre = None
        old = self.head
        while old:
            if old.data == value:
                break
            pre = old
            old = old.nxt
        if old.data:
            if pre == None:
                pre = old.nxt
                del old
                return pre
            pre.nxt = old.nxt
            del old
        self.size -= 1
        return self.head
    
    def traversal(self):
        p = self.head
        while p:
            print(p.data)
            p = p.nxt

class DListNode: # 雙邊環狀鏈結串列
    
    def __init__(self, data = 0):
        self.data = data
        self.front = None # 下個節點
        self.back = None # 上個節點
        
class DLinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0
        
    def length(self):
        return self.size
    
    def append(self, value):
        p = self.head
        node = DListNode(value)
        if p == None:
            self.head = node
        else:
            while p:
                if self.size < 2:
                    node.front = p
                    node.back = p
                    p.front = node
                    p.back = node
                else:
                    node.front = self.head # 設定新增節點的前後節點
                    node.back = p
                    p.front.back = node # 先把原節點的下個節點之前設為新節點
                    p.front = node
                p = p.front
                if p.front == self.head: # 新增完結點回到第一個節點並結束
                    break
        self.size += 1
                
    def insert(self, p, value):
        node = DListNode(value)
        node.front = p.front
        node.back = p
        p.front.back = node
        p.front = node
        self.size += 1
        
        
    def find(self, value):
        p = self.head
        while p:
            if p.data == value:
                return p
            p = p.front
            if p.front == self.head: # 找過一輪若沒找到則回傳None並結束
                return None
    
    def delete(self, value):
        pre = None
        old = self.head
        while old:
            if old.data == value:
                break
            pre = old
            old = old.front
        if old.data:
            if pre == None:
                pre = old.front
                pre.back = old.back
                del old
                return pre
            pre.front = old.front
            del old
        self.size -= 1
        return self.head
    
    def traversal(self):
        p = self.head
        while p:
            print(p.data)
            p = p.front
            if p == self.head:
                break   