# https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=daily-question&envId=2024-01-17
from typing import List
# Complexity of the following code is O(n)
def main():
    arr1:List[int]
    arr2:List[int]
    arr3:List[int]
    
    arr1 = [1, 2, 2, 1, 1, 3]
    arr2 = [1, 2]
    arr3 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    print(unique_occurences(arr1))
    print(unique_occurences(arr2))    
    print(unique_occurences(arr3))
    
    
def unique_occurences(arr:List[int])->bool:
    map = {}
    for num in arr:
        map[num] = map.get(num,0)+1
    	
    unique = set(map.values())
    return len(unique) == len(map)
    
    
if __name__ == '__main__':
    main()
    
    
# Complexity of the following code is O(n*logn)
def uniqueOccurrences(arr: List[int]) -> bool:
    map = {}
    for num in arr:
        map[num] = map.get(num,0)+1
    	
    array = list(map.values())
    array.sort()
    m = len(array)
    for i in range(0, m - 1):
        if array[i] == array[i+1]:
            return False
    return True