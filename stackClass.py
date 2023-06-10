class Stack: # 堆疊類別
    
    def __init__(self):
        self.item = []
    
    maximum = float("inf")
    def isFull(self): # 堆疊已滿
        return len(self.item) >= Stack.maximum
    
    def isEmpty(self): # 堆疊已空
        return len(self.item) == 0
    
    def push(self, value): # 推入堆疊
        if not self.isFull():
            self.item.append(value)
        
    def pop(self): # 推出堆疊
        if not self.isEmpty():
            return self.item.pop()
        
    def peek(self): # 查看堆疊最上方元素
        return self.item[-1]

# 把運算式由中序式轉換為後序式    
def op(ch): # 判定是否為運算元
    if ch.isalpha(): 
        return True
    return False

def in_to_post(infix): # 轉換函數
    # 按運算子執行優先順序編列value
    ops = {"(" : 0, "+" : 1, "-" : 1, "*" : 2, "/" : 2}
    postfix = [] # 串列postfix存放後序式
    opStack = Stack() # 堆疊opStack存放運算子
    for token in infix: # 走訪輸入之中序式字串
        if op(token): # 若碰到運算元就存入postfix
            postfix.append(token)
        elif token == "(": # 左括弧推入opStack
            opStack.push(token)
        elif token == ")": # 碰到右括弧開始從opStack推出運算子到postfix
            while not opStack.isEmpty():
                element = opStack.pop()
                if element == "(": # 碰到左括弧停止postfix繼續存放
                    break
                postfix.append(element)
        elif token in ops: # 推入opStack的運算子value小的在上面
            while not opStack.isEmpty():
                if ops[opStack.peek()] >= ops[token]:
                    element = opStack.pop()
                    postfix.append(element)
                else:
                    break
            opStack.push(token) # opStack推入運算子
    while not opStack.isEmpty(): # opStack剩餘運算子推出至postfix
        element = opStack.pop()
        postfix.append(element)
    return postfix

# print("".join(in_to_post("A+B*C-D/E")))

# 計算後序式的值
operands = {"A":2,"B":5,"C":4,"D":6,"E":3} # 運算元
operators = {"+","-","*","/"} # 運算子
def cal(pf):
    equation = Stack() # 堆疊equation紀錄計算後的值
    for token in pf:
        if token in operands: # 運算元均推入equation
            equation.push(operands[token])
        elif token in operators: # 碰到運算子就把equation裡的值推出來計算
            e1 = equation.pop()
            e2 = equation.pop()
            if token == "+":    
                equation.push(e2 + e1)
            elif token == "-":    
                equation.push(e2 - e1)
            elif token == "*":    
                equation.push(e2 * e1)
            elif token == "/":    
                equation.push(e2 / e1)
    return equation.item[0]
            
print(cal("AB+C*DE/-"))