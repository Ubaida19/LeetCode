# https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=daily-question&envId=2024-01-14

def main():
	s1 = input()
	s2 = input()
	print(close_strings(s1, s2))


def close_strings(word1, word2):
	n = len(word1)
	m = len(word2)
	if n != m:
		return False
	
	word1_list = [0]*26
	word2_list = [0]*26
	
	for i in range(n):
		word1_list[ord(word1[i]) - ord('a')] += 1
		word2_list[ord(word2[i]) - ord('a')] += 1
	
	for i in range(26):
		if (word1_list[i] == 0 and word2_list[i] != 0) or (word1_list[i] != 0 and word2_list[i] == 0):
			return False
	word1_list.sort()
	word2_list.sort()
	
	for i in range(26):
		if word1_list[i] != word2_list[i]:
			return False
	
	return True


if __name__ == '__main__':
	main()
	