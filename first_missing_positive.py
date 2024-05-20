from typing import List

def first_missing_positive(nums):
    i = 0
    while i < len(nums):
        if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
            temp = nums[i]
            nums[i], nums[temp - 1] = nums[temp - 1], nums[i]  # Swap
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1


def main():
    print(first_missing_positive([3,4,-1,1]))
    print(first_missing_positive([1,2,0]))
    print(first_missing_positive([7,8,9,11,12]))

main()