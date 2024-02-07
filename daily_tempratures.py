from typing import List

def main():
    temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]
    print(daily_tempratures(temperatures1))
    temperatures2 = [30, 40, 50, 60]
    print(daily_tempratures(temperatures2))
    temperatures3 = [30,60,90]
    print(daily_tempratures(temperatures3))
def daily_tempratures(temperatures:List[int])->List[int]:    
    result:List[int]
    length = len(temperatures)
    result = [0] * length
    stack = []
    for i in range(length):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            index = stack.pop()
            result[index] = i - index
        stack.append(i)
    return result
if __name__ == '__main__':
    main()