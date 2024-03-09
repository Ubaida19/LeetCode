from typing import List
def getCommon(nums1: List[int], nums2: List[int]) -> int:
    length1 = len(nums1)
    length2 = len(nums2)
    i = 0
    j = 0
    while i<length1 and j<length2:
        if nums1[i]<nums2[j]:
            i+=1
        elif nums1[i]>nums2[j]:
            j+=1
        elif nums1[i]==nums2[j]:
            return nums1[i]
    return -1


def main():
    nums1 = [1,2,3]
    nums2 = [2,4]
    print(getCommon(nums1,nums2))
    
    nums1 = [1,2,3,6]
    nums2 = [2,3,4,5]
    print(getCommon(nums1,nums2))


if __name__ == '__main__':
    main()