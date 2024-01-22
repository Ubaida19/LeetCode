# https://leetcode.com/problems/set-mismatch/description/?envType=daily-question&envId=2024-01-22
from typing import List
def main():
    nums1 = [1,2,2,4]
    print(findErrorNums(nums1))
    nums2 = [1,1]
    print(findErrorNums(nums2))
    nums3 = [2,2]
    print(findErrorNums(nums3))
    nums3 = [1,2,3,4,4,6]
    print(findErrorNums(nums3))
    nums4 = [3,2,3,4,6,5]
    print(findErrorNums(nums4))
    
    
def findErrorNums(nums: List[int]) -> List[int]:
    length = len(nums)
    missing:int = -100000
    duplicate:int = -10000
    
    freq = [0] * (length + 1)       # Frequency array
    for num in nums:
        freq[num] += 1
    freq_length = len(freq)
    for i in range(1, freq_length):
        if freq[i] == 0:
            missing = i
        if freq[i] > 1:            
            duplicate = i
    return [duplicate, missing]

if __name__ == '__main__':
    main()
    