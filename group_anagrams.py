from typing import List
def main():
    strs1 = ["eat","tea","tan","ate","nat","bat"]
    print(group_anagrams(strs1))
    
    strs2 = [""]
    print(group_anagrams(strs2))
    
    strs3 = ["a"]
    print(group_anagrams(strs3))
    
def group_anagrams(strs:List[str])->List[List[str]]:
    anagrams = {}
    
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word].append(word)
            
    return list(anagrams.values())
    
    
if __name__ == '__main__':
    main()