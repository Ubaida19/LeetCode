from typing import List
def main():
    words1 = ["abc","car","ada","racecar","cool"]
    print(first_palindrome(words1))
    words2 = ["notapalindrome","racecar"]
    print(first_palindrome(words2))
    word3 = ["def","ghi"]
    print(first_palindrome(word3))
    
def first_palindrome(words:List[str])->str:
    result:str = ""
    for word in words:
        length = len(word)
        first:int = 0
        last:int = length-1
        while first < last and word[first] == word[last]:
            first += 1
            last -= 1
        if word[first] == word[last]:
            return word
    return result
    
if __name__ == '__main__':
    main()	