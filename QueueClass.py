class Queue: # 佇列類別
    
    def __init__(self):
        self.item = []
        
    def isEmpty(self): # 佇列已空
        return len(self.item) == 0
    
    def isFull(self): # 佇列已滿
        return False
    
    def enQueue(self, value): # 進入佇列
        if not self.isFull():
            self.item.append(value)
        
    def deQueue(self): # 離開佇列
        if not self.isEmpty():
            return self.item.pop(0)
        return None