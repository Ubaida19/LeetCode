def is_isomorphic(s: str, t: str) -> bool:
    hash_map = {}
    my_set = set()
    for i in range(len(s)):
        s_char = s[i]
        t_char = t[i]
        # If we have seen s_char before,
        if s_char in hash_map:
            # If the char against s_char in hash_map is not t_char
            if hash_map[s_char] != t_char:
                return False
        # s_char is not encountered,
        else:
            # But t_char is encountered before:
            if t_char in my_set:
                return False
            # Add them to the hash_map and set respectively.
            hash_map[s_char] = t_char
            my_set.add(t_char)
    return True


def main():
    str1 = "ACAB"
    str2 = "XCXY"
    s1 = 'egg'
    t1 = 'add'
    print(is_isomorphic(s1, t1))

    s2 = "foo"
    t2 = "bar"
    print(is_isomorphic(s2, t2))

    s3 = 'paper'
    t3 = 'title'
    print(is_isomorphic(s3, t3))

    s4 = 'bbbaaaba'
    t4 = "aaabbbba"
    print(is_isomorphic(s4, t4))


if __name__ == '__main__':
    main()