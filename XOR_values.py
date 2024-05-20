from typing import List

def xor_subset(subset: List[int]) -> int:
    """Calculate the XOR of a single subset."""
    result = 0
    for num in subset:
        result ^= num
    return result

def xor(nums: List[int]) -> int:
    """Calculate the XOR of all subsets."""
    n = len(nums)
    all_subset = []
    
    for i in range(2**n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(nums[j])
        all_subset.append(subset)
    
    overall_xor = 0
    for subset in all_subset:
        overall_xor += xor_subset(subset)
    
    return overall_xor


def main():
    print(xor([1,3]))
    print(xor([5, 1, 6]))
    print(xor([3,4,5,6,7,8]))
    
    


main()
