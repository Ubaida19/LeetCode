from typing import List
def main():
    arr1 = [5,5,4]
    print(find_least_num_Of_unique_ints(arr1,1))
    arr2 = [4,3,1,1,3,3,2]
    print(find_least_num_Of_unique_ints(arr2,3))

def find_least_num_Of_unique_ints(arr:List[int],k:int)->int:
    # {'1': 2, '2': 1, '3': 3, '4': 1}
    # {'2': 1,'4': 1,'1': 2,'3': 3}
    freq = {}
    for num in arr:
        freq[num] = freq.get(num,0) + 1
    sorted_freq = sorted(freq.items(),key = lambda x:x[1])
    for key,value in sorted_freq:
        if value<=k:
            k -= value
            del freq[key]
        else:
            break
    return len(freq)

if __name__ == '__main__':
    main()