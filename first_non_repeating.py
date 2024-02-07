def main():
    string1 = "leetcode"
    print(first_unique_char(string1))
    string2 = "loveleetcode"
    print(first_unique_char(string2))
    string3 = "aabb"
    print(first_unique_char(string3))
    string4 = "abuubaida"
    print(first_unique_char(string4))
    
def first_unique_char(s:str)->int:
    hashmap = {}
    for char in s:
        hashmap[char] = hashmap.get(char,0)+1

    for key,value in hashmap.items():
        if value == 1:
            return s.index(key)    
    return -1
if __name__=='__main__':
    main()