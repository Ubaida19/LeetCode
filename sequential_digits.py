from typing import List
def main():
    print(sequential_digits(100,300))
    print(sequential_digits(1000,13000))
    
def sequential_digits(low:int, high:int)->List[int]:
    nums = [
            12, 23, 34, 45, 56, 67, 78, 89,
            123, 234, 345, 456, 567, 678, 789,
            1234, 2345, 3456, 4567, 5678, 6789,
            12345, 23456, 34567, 45678, 56789,
            123456, 234567, 345678, 456789,
            1234567, 2345678, 3456789,
            12345678, 23456789,
            123456789
            ]
    
    result=[]
    for num in nums:
        if num >= low and num <= high:
            result.append(num)
    return result

if __name__ == '__main__':
    main()