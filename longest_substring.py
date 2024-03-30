def length_of_longest_substring(s:str) -> int:
    unique_chars = set()
    max_length = 0
    left = 0
    length = len(s)
    for right in range(length):
        if s[right] not in unique_chars:
            unique_chars.add(s[right])
            max_length = max(max_length, right-left+1)
        else:
            while s[right] in unique_chars:
                unique_chars.remove(s[left])
                left += 1
            unique_chars.add(s[right])
    return max_length


def main():
    str5 = "dvdf"
    print(length_of_longest_substring(str5))
    str4 = " "
    print(length_of_longest_substring(str4))
    str1 = "abcabcbb"
    print(length_of_longest_substring(str1))

    str2 = "bbbbb"
    print(length_of_longest_substring(str2))

    str3 = "pwwkew"
    print(length_of_longest_substring(str3))



if __name__ == '__main__':
    main()