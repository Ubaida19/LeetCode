def custom_sort_string(order:str,s:str)->str:
    # result = ""
    # hash={}
    # {'c': 1, 'b': 1, 'a': 1}
    # for char in order:
    #     if char in hash:
    #         hash[char] += 1
    #     else:
    #        hash[char] = 1
    # result=''
    # for char in s:
    #    if char in hash:
    result = ''
    hash = {}
    # {'a': 1, 'b': 1, 'c': 1,'d':1}
    for char in s:
        if char in hash:
            hash[char] += 1
        else:
            hash[char] = 1
    for char in order:
        if char in hash:
            result += char * hash[char]
            hash[char] = 0
    for char in hash:
            result += char * hash[char]
    return result

def main():
    order1 = "cba"
    s1 = "abcdaf"
    print(custom_sort_string(order1,s1))
    
    order2 = "bcafg"
    s2 = "abcd"
    print(custom_sort_string(order2,s2))
if __name__=='__main__':
    main()