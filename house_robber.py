# https://leetcode.com/problems/house-robber/description/?envType=daily-question&envId=2024-01-21
from typing import List
def main():
    nums1 = [1, 2, 3, 1]
    nums2 = [2, 7, 9, 3, 1]
    nums3 = [2, 1, 1, 2]
    nums4 = [6,3,10,8,2,10,3,5,10,5,3]
    print(rob(nums1))
    print(rob(nums2))
    print(rob(nums3))
    print(rob(nums4))

def rob(nums:List[int]):
    previous_max = 0 # sums excluding the current house 
    current_max = 0  # sums including the current house
    
    for money in nums:
        temp = current_max
        current_max = max((previous_max + money), current_max)
        previous_max = temp    
    return current_max
if __name__ == '__main__':
    main()