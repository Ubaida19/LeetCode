from typing import List
def largest_local(grid:List[List[int]]):
    n = len(grid)
    max_local = [[0] * (n - 2) for _ in range(n - 2)]
    
    for i in range(n-2):
        for j in range(n-2):
            max_val = float('-inf')
            for k in range(0,3):
                for l in range(0,3):
                    max_val = max(max_val, grid[i+k][j+l])
            max_local[i][j] = max_val
    return max_local
def main(): 
    grid1 = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
    print(largest_local(grid1))
    
    #grid2 = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    #print(largest_local(grid2))
    
main()