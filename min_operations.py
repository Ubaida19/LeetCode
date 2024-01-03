# LeetCode problem # 2870: Minimum Number of Options to make an array empty
from typing import List


def main():
	print(min_operations([2, 3, 3, 2, 2, 4, 2, 3, 4]))
	print(min_operations([2, 1, 2, 2, 3, 3]))
	print(min_operations([3, 3]))
	print(min_operations([14, 12, 14, 14, 12, 14, 14, 12, 12, 12, 12, 14, 14, 12, 14, 14, 14, 12, 12]))


def min_operations(nums: List[int]) -> int:
	max_number = max(nums)
	count_array = [0] * (max_number + 1)
	for number in nums:
		count_array[number] += 1
		
	count_of_operations: int = 0
	for count in count_array:
		if count == 1:
			return -1
		count_of_operations += ((count // 3) + (count % 3+1)//2)
		
	return count_of_operations


if __name__ == '__main__':
	main()
	