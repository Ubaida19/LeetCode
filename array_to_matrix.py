# LeetCode Problem # 2610: Array to Matrix with Conditions
def main():
	nums1 = [1, 3, 4, 1, 2, 3, 1]
	nums2 = [2, 1, 1]
	nums3 = [1, 2, 3, 4]
	nums4 = [9, 8, 8, 4, 9, 8, 8, 3, 9]
	print(find_matrix(nums1))
	print(find_matrix(nums2))
	print(find_matrix(nums3))
	print(find_matrix(nums4))


def find_matrix(nums):
	freq = [0] * (len(nums)+1)
	matrix = []
	
	for num in nums:
		if freq[num] >= len(matrix):
			matrix.append([])
		matrix[freq[num]].append(num)
		freq[num] += 1
	return matrix


if __name__ == '__main__':
	main()
	