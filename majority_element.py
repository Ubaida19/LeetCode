from typing import List
import math
def main():
    nums1 = [3,2,3]
    print(majority_element(nums1))
    nums2 = [2,2,1,1,1,2,2]
    print(majority_element(nums2))
    
    
def majority_element(nums:List[int]):
    count = {}
    max_count = len(nums)//2
    for num in nums:
        count[num] = count.get(num,0)+1
    for key,value in count.items():
        if value > max_count:
            return key
if __name__ == '__main__':
    main()