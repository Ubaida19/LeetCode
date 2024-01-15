# https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/?envType=daily-question&envId=2024-01-15
from typing import List


def main():
	matches1 = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
	matches2 = [[2, 3], [1, 3], [5, 4], [6, 4]]
	print(find_winners(matches1))
	print(find_winners(matches2))


def find_winners(matches: List[List[int]]) -> List[List[int]]:
	no_losses = set()
	one_loss = set()
	more_than_one_loss = set()
	
	for match in matches:
		winner = match[0]
		loser = match[1]
		if winner not in one_loss and winner not in more_than_one_loss:
			no_losses.add(winner)
			
		if loser in no_losses:
			no_losses.remove(loser)
			one_loss.add(loser)
		elif loser in one_loss:
			one_loss.remove(loser)
			more_than_one_loss.add(loser)
		elif loser in more_than_one_loss:
			continue
		else:
			# Means that no loss is found for current loser
			one_loss.add(loser)
			
	answer = [sorted(list(no_losses)), sorted(list(one_loss))]
	return answer


if __name__ == '__main__':
	main()
	