def main():
	s = input('Enter string: ')
	k = int(input('Enter k: '))
	print(get_length_of_optimal_compression(s, k))
	

def get_length_of_optimal_compression(s: str, k: int) -> int:
	# OPT(i, j) = minimum string length of first i characters in [s], removing j <= [k] characters.
	
	# Sub-problem relation: consider the last block of characters. you can either:
	
	# (i) remove one element from it - OPT(i-1, j-1)
	
	# (ii) skip this block, and assume it doesn't merge - OPT(i-b(i), j) + length[b(i)]
	# b(i) = distance to the previous block
	# length[b(i)] = length of the merged block
	# (iii) merge it with 1, 2, ... k previous blocks, where there are k previous blocks of the same element
	
	# Base cases:
	# OPT(i, j) = 0 if i <= j
	# OPT(i, 0) = length of the first i characters
	
	n = len(s)
	values = [[0]*(k+1) for _ in range(n+1)]  # rows are the characters, columns are removal number
	
	# Data structure representation:
	# [x1, x2, x3, ...], with [xi] representing the number of characters in the i-th block
	data = []
	
	length = 0  # length of the compressed string
	
	# info on the current block
	block_char = None
	block_start = 0
	prev_blocks_length = 0  # for convenience, I save the sum of all previous block's lengths (not the current one)
	
	block_number = -1  # block number
	block_numbers = {}  # character [c] -> list of indices corresponding to data
	
	for i, ch in enumerate(s):
		
		# Case 1: we enter a new block
		if ch != block_char:
			block_number += 1
			block_char = ch
			if block_char not in block_numbers:
				block_numbers[block_char] = []
			
			block_numbers[block_char].append((block_number, i+1))  # add new block info
			block_start = i  # new starting block index
			data.append(1)  # with a new block, we create a new entry in data
			prev_blocks_length = length
			length += 1  # creates a new letter in the encoding
		
		# Case 2: we are still in the same block
		else:
			data[-1] += 1
			if data[-1] == 100 or data[-1] == 10 or data[-1] == 2:
				length += 1
		
		# Base case:
		values[i+1][0] = length
		
		# We can now populate the entire row of OPT(i+1, j)'s from 1 -> k
		for j in range(1, k+1):
			
			# Case (i) - remove one element
			minimum = values[i][j-1]
			
			# Case (ii) - keep the entire block
			minimum = min(minimum, values[block_start][j] + (length - prev_blocks_length))
			
			# Case (iii) - merging 1, 2, ... blocks together from the end
			if ch in block_numbers:
				b = len(block_numbers[ch]) - 1
				merge_k = 0  # total characters to be removed for the next merge
				num_chars = data[block_numbers[ch][b][0]]  # store the total characters
				
				while b > 0 and merge_k < j:
					right, _ = block_numbers[ch][b]
					left, idx = block_numbers[ch][b-1]
					num_chars += data[left]
					
					b -= 1  # next block
					
					for m in range(left+1, right):  # (left, right)
						merge_k += data[m]
					
					if merge_k <= j:  # valid merge, now compute the summation
						summation = 1
						if num_chars >= 100:
							summation += 1
						if num_chars >= 10:
							summation += 1
						if num_chars >= 2:
							summation += 1
						minimum = min(minimum, values[idx-1][j - merge_k] + summation)
			
			values[i+1][j] = minimum  # populate
	
	# OPT(n, k) is the solution to the original problem
	return values[-1][-1]


if __name__ == '__main__':
	main()
	