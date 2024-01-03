from typing import List


def main():
	bank1 = ["011001", "000000", "010100", "001000"]
	bank2 = ["000", "111", "000"]
	print(number_of_beams(bank1))
	print(number_of_beams(bank2))


def number_of_beams(bank: List[str]) -> int:
	length = len(bank)
	counts_of_one = [0] * length     # [3, 0, 2, 1]       [0, 3, 0]
	index = 0
	for string in bank:
		for char in string:
			if char == '1':
				counts_of_one[index] += 1
		index += 1

	length_of_one = len(counts_of_one)
	beam = 0
	for i in range(length_of_one-1):
		j = i + 1
		while counts_of_one[j] <= 0 and j < length_of_one-1:
			j += 1
		beam += counts_of_one[i] * counts_of_one[j]
	return beam


if __name__ == '__main__':
	main()
	