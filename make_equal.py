# Leet code problem number 1897: Redistribute Characters to Make All Strings Equal
from typing import List


def main():
	num = int(input('Enter number of strings: '))
	words: List[str] = ['0'] * num
	for i in range(num):
		words[i] = input(f'Enter string {i+1}: ')
	print(make_equal(words))


def make_equal(words: List[str]) -> bool:
	n: int = len(words)
	alphabet: List[int] = [0] * 26
	for word in words:
		for ch in word:
			alphabet[ord(ch)-ord('a')] += 1
	
	for val in alphabet:
		if val % n != 0:
			return False
	return True


if __name__ == '__main__':
	main()
	