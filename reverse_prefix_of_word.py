def reverse_prefix(word: str, ch: str) -> str:
    length = len(word)
    i: int = 0
    while i < length and word[i] != ch:
        i += 1
    if i == length:
        return word
    else:
        reverse_string = list(word[0: i+1])
        reverse_string.reverse()
        reverse = "".join(reverse_string)
        result = reverse + word[i+1:]
        return result


def main():
    word1 = "abcdefd"
    ch1 = "d"
    print(reverse_prefix(word1, ch1))

    word2 = "xyxzxe"
    ch2 = "z"
    print(reverse_prefix(word2, ch2))

    word3 = "abcd"
    ch3 = "z"
    print(reverse_prefix(word3, ch3))


main()
