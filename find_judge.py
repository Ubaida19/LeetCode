from typing import List
def main():
    trust2 = [[1,3],[2,3]]
    print(find_judge(3,trust2))
    
    trust3 = [[1,3],[2,3],[3,1]]
    print(find_judge(3,trust3))
    
    trust4 = [(1,2)]
    print(find_judge(2,trust4))
    
    trust5 = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    print(find_judge(4,trust5))
    
def find_judge(n:int,trust:List[List[int]])->int:
    trusting = [0] * (n + 1)
    trusted = [0] * (n + 1)
    
    for x,y in trust:
        trusting[x] += 1
        trusted[y] += 1
    
    for i in range(1, n + 1):
        if trusting[i] == 0 and trusted[i] == n - 1:
            return i
    
    return -1


if __name__ == '__main__':
    main()