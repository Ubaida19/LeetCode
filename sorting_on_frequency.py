def main():
    print(frequency_sort("tree"))
    print(frequency_sort("cccaaa"))
    print(frequency_sort("Aabb"))
    print(frequency_sort("abaccadeeefaafcc"))
    
def frequency_sort(s:str)->str:
    hash = {}
    for char in s:
        hash[char] = hash.get(char,0)+1
    result:str = ""
    sorted_frequency = sorted(hash.items(),key = lambda x:x[1],reverse = True)
    for item in sorted_frequency:
        result = result + (item[0]*item[1])
    return result
if __name__=='__main__':
    main()