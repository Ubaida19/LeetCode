# LeetCode problem # 1624: Largest Substring Between Two Equal Characters
from typing import List


def main():
	s: str
	s = input('Enter string: ')
	print(get_max_length_between_equal_chars(s))


def get_max_length_between_equal_chars(s: str) -> int:
	n = len(s)
	if n == 2:
		return 0
	elif n < 2:
		return -1
	first = 0
	length: int = 0
	count: int = 0
	while count < n:
		last = n - 1
		while s[last] != s[first] and first < last:
			last -= 1
		
		if s[last] == s[first]:
			if last - first > length:
				length = last - first - 1
		count += 1
		first += 1
	if length == 0:
		return -1
	return length


if __name__ == '__main__':
	main()
	