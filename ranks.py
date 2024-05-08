from typing import List


def relative_ranks(nums: List[int]):
    num_dict = {}
    for i in range(len(nums)):
        num_dict[i] = nums[i]

    num_dict = sorted(num_dict.items(), key=lambda item: item[1], reverse=True)
    ranks = ['0']*len(nums)
    i = 1

    for key, value in num_dict:
        if i <= 3:
            if i == 1:
                ranks[key] = 'Gold Medal'
                i = i+1
            elif i == 2:
                ranks[key] = 'Silver Medal'
                i = i + 1
            elif i == 3:
                ranks[key] = 'Bronze Medal'
                i = i + 1
        else:
            ranks[key] = str(i)
            i = i+1
    return ranks

def main():
    print(relative_ranks([5, 4, 3, 2, 1]))
    print(relative_ranks([10, 3, 8, 9, 4]))


if __name__ == "__main__":
    main()
