from typing import List


def product_except_self(nums:List[int]) -> List[int]:
    length = len(nums)
    result = [0]*length
    left = [1] * length
    right = [1] * length

    for i in range(1,length):
        left[i] = left[i-1]*nums[i-1]
    for j in range(length-2, -1, -1):
        right[j] = right[j+1]*nums[j+1]

    for i in range(length):
        result[i] = left[i]*right[i]
    return result


def main():
    nums1 = [1, 2, 3, 4]
    print(product_except_self(nums1))

    nums2 = [-1, 1, 0, -3, 3]
    print(product_except_self(nums2))


if __name__ == '__main__':
    main()
