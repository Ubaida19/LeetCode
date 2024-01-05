# https://leetcode.com/problems/longest-increasing-subsequence/?envType=daily-question&envId=2024-01-05

def main():
	print(longest_increasing_sequence([10, 9, 2, 5, 3, 7, 101, 18]))     # Output: 4
	print(longest_increasing_sequence([0, 1, 0, 3, 2, 3]))               # Output: 4
	print(longest_increasing_sequence([7, 7, 7, 7, 7, 7, 7]))            # Output: 1
	# own
	print(longest_increasing_sequence([0, 2, 1, 0,  3, 2, 3]))           # Output: 4
	
	print(longest_increasing_sequence([1, 3, 6, 7, 9, 4, 10, 5, 6]))      # Output: 6
	
	
def longest_increasing_sequence(nums):
	n = len(nums)
	length_of_sequence = [1] * n
	for i in range(n):
		for j in range(i):
			if nums[i] > nums[j]:
				current = length_of_sequence[j] + 1
				length_of_sequence[i] = max(length_of_sequence[i], current)
				
	return max(length_of_sequence)


if __name__ == '__main__':
	main()
	