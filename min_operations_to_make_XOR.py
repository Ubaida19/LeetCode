from typing import List


def min_operations(nums: List[int], k: int) -> int:
    final_xor = 0
    for num in nums:
        final_xor ^= num
    count: int = 0
    while k or final_xor:
        if (k % 2) != (final_xor % 2):
            count += 1
        k = k//2
        final_xor = final_xor // 2
    return count

def main():
    nums1 = [2, 1, 3, 4]
    k1 = 1
    print(min_operations(nums1, k1))

    nums2 = [2,0,2,0]
    k2 = 0
    print(min_operations(nums2, k2))

main()
