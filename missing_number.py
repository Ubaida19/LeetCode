from typing import List
def main():
    nums1 = [3,0,1]
    print(missing_number(nums1))
    nums2 = [0,1]
    print(missing_number(nums2))
    nums3 = [9,6,4,2,3,5,7,0,1]
    print(missing_number(nums3))

def missing_number(nums:List[int])->int:
    length = len(nums)
    total_sum = (length*(length+1))//2
    nums_sum:int = 0
    for num in nums:
        nums_sum += num
    return total_sum - nums_sum
    
if __name__ == '__main__':
    main()