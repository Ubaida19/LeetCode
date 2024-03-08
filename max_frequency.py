from typing import List
def max_freq_elements(nums:List[int])->int:
    hash = {}
    for num in nums:
        if num in hash:
            hash[num] += 1
        else:
            hash[num] = 1
    max_freq = 0
    result = 0
    for key,value in hash.items():
        if value > max_freq:
            max_freq = value
            result = value
        elif value == max_freq:
            result += value
    return result

def main():
    nums1 = [1,2,2,3,1,4]
    print(max_freq_elements(nums1))
    nums2 = [1,2,3,4,5]
    print(max_freq_elements(nums2))
    
if __name__ == '__main__':
    main()