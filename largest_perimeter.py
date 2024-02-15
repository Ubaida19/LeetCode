from typing import List
def main():
    nums1 = [5,5,5]
    print(largest_perimeter(nums1))
    nums2 = [1,12,1,2,5,50,3]
    print(largest_perimeter(nums2))
    nums3 = [5,5,50]
    print(largest_perimeter(nums3))
    nums4 = [1,1,2]
    print(largest_perimeter(nums4))
    nums5 = [1,5,1,7]
    print(largest_perimeter(nums5))
def largest_perimeter(nums:List[int])->int:
    nums.sort()
    ans:int = 0
    length = len(nums)
    for i in range(length-1,1,-1):
        sides_arr = nums[0:i]
        if nums[i] < sum(sides_arr):
            ans = sum(sides_arr,nums[i])
            return ans
    return -1
if __name__ == "__main__":
    main()