# LeetCode problem # 455: Assign Cookies
from typing import List


def main():
	greed = [1, 2, 3]
	cookies = [1, 1]
	print(find_content_children(greed, cookies))


def find_content_children(greed: List[int], cookies: List[int]) -> int:
	greed.sort()
	cookies.sort()
	i: int = 0
	j: int = 0
	count: int = 0
	
	while i < len(greed) and j < len(cookies):
		if cookies[i] >= greed[j]:
			count += 1
			i += 1
		j += 1


if __name__ == '__main__':
	main()
	