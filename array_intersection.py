from typing import List
def intersection(nums1:List[int],nums2:List[int])->List[int]:
    return list(set(nums1) & set(nums2))
    
    
def main():
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(intersection(nums1,nums2))
    nums3 = [4,9,5]
    nums4 = [9,4,9,8,4]
    print(intersection(nums3,nums4))

if __name__ == '__main__':
    main()
