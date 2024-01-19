# https://leetcode.com/problems/minimum-falling-path-sum/description/?envType=daily-question&envId=2024-01-19
from typing import List
def main():
    matrix1 = [[2,1,3],[6,5,4],[7,8,9]]
    matrix2 = [[-19,57],[-40,-5]]
    print(min_falling_path_sum(matrix1))
    print(min_falling_path_sum(matrix2))
    
def min_falling_path_sum(matrix:List[List[int]]) -> int:
    n=len(matrix)
    m=len(matrix[0])
    for r in range(n):
        for c in range(m):
            if r>0 and 0<=c-1 and c+1<m:
                matrix[r][c]=min(matrix[r][c]+matrix[r-1][c],matrix[r][c]+matrix[r-1][c+1],matrix[r][c]+matrix[r-1][c-1])
            elif r>0 and c-1==-1:
                matrix[r][c]=min(matrix[r][c]+matrix[r-1][c],matrix[r][c]+matrix[r-1][c+1])
            elif r>0 and c+1==m:
                matrix[r][c]=min(matrix[r][c]+matrix[r-1][c],matrix[r][c]+matrix[r-1][c-1])

    return min(matrix[n-1])           

if __name__ == '__main__':
    main()