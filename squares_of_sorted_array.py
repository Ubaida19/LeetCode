from typing import List
def sorted_square(nums:List[int])->List[int]:
    left = 0
    right = len(nums) - 1
    result=[]
    while left <= right:
        if abs(nums[left]) < abs(nums[right]):
            result.append(nums[right]**2)
            right -= 1
        else:
            result.append(nums[left]**2)
            left += 1
    return result[::-1]
def main():
    nums1 = [-4,-1,0,3,10]
    print(sorted_square(nums1))
    nums2 = [-7,-3,2,3,11]
    print(sorted_square(nums2))
    
if __name__=="__main__":
    main()
