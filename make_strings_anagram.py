# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/?envType=daily-question&envId=2024-01-13


def main():
	s1: str
	s2: str
	s1 = input()
	s2 = input()
	print(min_steps(s1, s2))


def min_steps(s1: str, s2: str) -> int:
	steps: int = 0
	s1_char_list = {}
	s2_char_list = {}
	
	for char in s1:
		s1_char_list[char] = s1_char_list.get(char, 0) + 1
	for char in s2:
		s2_char_list[char] = s2_char_list.get(char, 0) + 1
	
	for char in s1_char_list:
		if s1_char_list[char] - s2_char_list.get(char, 0) > 0:
			steps += s1_char_list[char] - s2_char_list.get(char, 0)
	return steps


if __name__ == '__main__':
	main()
	