from typing import List


def main():
    nums1 = [1,3,4,8,7,9,3,5,1]
    # [1,1,3,3,4,5,7,8,9]
    print(divide_array(nums1,2))
    
    
def divide_array(nums:List[int], k:int) -> List[List[int]]:
    result = []
    nums.sort()
    length = len(nums)
    
    for i in range(0,length,3):
        if nums[i+2]-nums[i]<=k:
            result.append([nums[i],nums[i+1],nums[i+2]])
        else:
            return []
    return result
if __name__ == '__main__':
    main()