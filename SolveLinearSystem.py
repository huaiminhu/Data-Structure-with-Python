def GaussJordanElimination(matrix): # 求解線性系統
    
    # 向下做消去法  
    for column in range(len(matrix[0]) - 1):
        for row in range(column + 1, len(matrix)):
            if matrix[column][column] != 0:
                # 做列運算
                matrix[row] -= (matrix[row][column] / matrix[column][column]) * matrix[column]
                # print(matrix)
                
    # 向上消去
    for column in range(len(matrix) - 1, 0, -1):
        for row in range(column - 1, -1, -1):
            if matrix[column][column] != 0:
                matrix[row] -= (matrix[row][column] / matrix[column][column]) * matrix[column]
                # print(matrix)
                
    # 各列除以對角線上係數得到解
    for column in range(len(matrix)):
        if matrix[column][column] != 0:
            matrix[column] /= matrix[column][column]
    
    return matrix[:, -1] # 效率為O(n ** 2)
        
import numpy as np            
if __name__ == "__main__":
    test = np.array([[1, 2, 3, 4],
                     [2, 2, 3, 4],
                     [2, 3, 4, 5]], dtype = float)
    print(GaussJordanElimination(test))