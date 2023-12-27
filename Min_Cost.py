def main():
	colors = input('Enter string: ')
	needed_time = [0] * len(colors)
	print('Enter array values: ')
	for i in range(len(colors)):
		needed_time[i] = int(input())
	res: int = min_cost(colors, needed_time)
	print('The total time is: ', res)
	
	
def min_cost(colors: str, needed_time) -> int:
	total_time = 0
	for i in range(1, len(colors)):
		if colors[i] == colors[i - 1]:
			total_time += min(needed_time[i], needed_time[i-1])
			needed_time[i] = max(needed_time[i], needed_time[i-1])
	return total_time


if __name__ == '__main__':
	main()
