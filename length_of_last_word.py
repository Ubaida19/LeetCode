def lengthOfLastWord(s: str)->int:
    length = len(s)
    char_occurred = False
    space_count = 0
    for i in range(length-1, -1, -1):
        if s[i] == " " and char_occurred:
            return length-i-1-space_count
        elif s[i] != ' ':
            char_occurred = True
        elif s[i] == ' ' and not char_occurred:
            space_count += 1
    return length-space_count
    #
    # words = s.strip().split(' ')
    # if not words:
    #     return 0
    # return len(words[-1])
    #
def main():
    s1 = "Hello World"
    print(lengthOfLastWord(s1))

    s2 = "   fly me   to   the moon  "
    print(lengthOfLastWord(s2))

    s3 = "luffy is still joyboy"
    print(lengthOfLastWord(s3))

    s4 = "fly"
    print(lengthOfLastWord(s4))


if __name__ == '__main__':
    main()
