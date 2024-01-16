# https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=daily-question&envId=2024-01-16


class RandomizedSet:
	def __init__(self):
		self.map = {}
	
	def insert(self, val: int) -> bool:
		if val not in self.map:
			self.map[val] = val
			return True
		return False
	
	def remove(self, val: int) -> bool:
		if val in self.map:
			self.map.pop(val)
			return True
		return False
	
	def get_random(self) -> int:
		import random
		return random.choice(list(self.map.keys()))


def main():
	obj = RandomizedSet()
	param1 = obj.insert(1)
	param2 = obj.remove(2)
	param3 = obj.get_random()
	print(param1)
	print(param2)
	print(param3)
	
	
if __name__ == '__main__':
	main()
