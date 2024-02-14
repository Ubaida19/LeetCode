from typing import List
def main():
    nums1 = [3,1,-2,-5,2,-4]
    print(rearrange_array(nums1))
    nums2 = [-1,1]
    print(rearrange_array(nums2))
    
def rearrange_array(nums:List[int])->List[int]:
    """
    positive_nums = []
    negative_nums = []
    for num in nums:
        if num > 0:
            positive_nums.append(num)
        else:
            negative_nums.append(num)
    result = []
    i:int = 0
    while i < len(nums)/2:
        result.append(positive_nums[i])
        result.append(negative_nums[i])
        i+=1
    return result
    """
    
    result = [0] * len(nums)
    positive_index = 0
    negative_index = 1
    for num in nums:
        if num > 0:
            result[positive_index] = num
            positive_index += 2
        elif num < 0:
            result[negative_index] = num
            negative_index += 2
    return result
if __name__ == '__main__':
    main()