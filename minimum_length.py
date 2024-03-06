def minimum_length(s:str):
    left = 0
    right = len(s) - 1
        
    while left < right and s[left] == s[right]:
        current = s[left]
        while left <= right and s[left] == current:
            left += 1
        while right >= left and s[right] == current:
            right -= 1
        
    return right - left + 1

def main():
    str1 = 'ca'
    print(minimum_length(str1))
    str2 = 'cabaabac'
    print(minimum_length(str2))
    str3 = "aabccabba"
    print(minimum_length(str3))
    
if __name__ == "__main__":
    main()